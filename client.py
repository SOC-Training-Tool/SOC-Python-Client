import grpc
from abc import ABC, abstractmethod

import threading
import time

import catan_pb2_grpc
import catan_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = catan_pb2_grpc.CatanServerStub(channel)

class Client:
    """
    Lighweight process that connects to a given game and plays using a specific strategy.
    Every update will be registered against the strategy state tracker,
    which is a specific instance for the client.
    In constrast, consults a strategy object (which can be shared between threads)
    to make game decisions.
    """

    def run(self, client_id, name, game_id, position, strategy):
      state_tracker = strategy.create_state_tracker()
      request = catan_pb2.SubscribeRequest(name=name, game_id=game_id) # TODO: Add position
      for response in stub.Subscribe(request):
        print(f'Player {name}, Game {game_id} received game update: {response.payload}')
        if str(response.payload).split(':')[0] == 'GAME OVER':
            break
        state_tracker.update(response)
        if name in response.action_requested_players:
            if strategy.should_request_state(state_tracker):
                state_request = catan_pb2.StateRequest(game_id, position)
                state = stub.GetState(state_request)
                state_tracker.update(state)
            move = strategy.get_move(self.state_tracker)
            print(f'Player {name}, client {client_id}, making move: {move}')
            stub.Move(catan_pb2.MoveRequest(move))
            stub.AcknowledgeGameStart()

class Player:


  def __init__(self, name, strategy):
    self.client_id_count = 0
    self.name = name
    self.strategy = strategy
    self.clients = []

  def play(self, game_id, position):
      """
      Registers the player to the given id at the given position.
      Creates a new client that connects to the given game.
      The client can than listen and respond to updates.
      """
      self.client_id_count += 1
      self.flush()
      args = (self.client_id_count, self.name, game_id, position, self.strategy)
      thread = threading.Thread(target=Client().run, args=args)
      self.clients.append(thread)
      thread.start()

  def flush(self):
    """
    Drops references to all clients that are no longer playing a game
    """
    self.clients = [c for c in self.clients if c.isAlive()]


class Strategy(ABC):
    """
    Determines what a player should do based on a game state (and optionally running state)
    """
    
    @abstractmethod
    def create_state_tracker(self):
        pass

    @abstractmethod
    def should_request_state(self):
        pass

    @abstractmethod
    def get_move(self,state_tracker):
        pass

class StatelessStrategy(Strategy):
    """
    The stateless strategy always requests the full state before making a move
    It's nested state tracker keeps track of the latest state received
    """

    class StateTracker:

        def __init__(self):
          self.state = None

        def update(self, state):
          self.state = state

    def create_state_tracker(self):
      return StatelessStrategy.StateTracker()

    def should_request_state(self):
      return True

    def get_move(self, state_tracker):
      return self.get_stateless_move(state_tracker.current_state)

    @abstractmethod
    def get_stateless_move(self, current_state):
      pass

class MyStrategy(StatelessStrategy):

    def get_stateless_move(self, current_state):
      # TODO Implement a strategy, where current state is a schema defined in CatanAI google doc
      # Should return some type of well defined move object
      return None




strategy = MyStrategy()
players = [Player("Dani", strategy), Player("Greg", strategy), Player("Ronnie", strategy), Player("Ariel", strategy)]

SIMULATIONS = 2

for _ in range(0, SIMULATIONS):
  response = stub.CreateGame(catan_pb2.CreateGameRequest())
  game_id = response.game_id
  for i, player in enumerate(players):
    player.play(game_id, position=i + 1)
  print(f'Start game {game_id}')
  stub.StartGame(catan_pb2.StartGameRequest(game_id=game_id))

has_active_games = True
while has_active_games:
  time.sleep(0.1)
  has_active_games = any([len(p.clients) > 0 for p in players])
  for player in players:
    player.flush()
