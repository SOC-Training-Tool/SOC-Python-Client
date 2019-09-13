# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import catan_pb2 as catan__pb2


class CatanServerStub(object):
  """All RPCs must have a request and response message, even if empty
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateGame = channel.unary_unary(
        '/soc.protos.CatanServer/CreateGame',
        request_serializer=catan__pb2.CreateGameRequest.SerializeToString,
        response_deserializer=catan__pb2.CreateGameResponse.FromString,
        )
    self.StartGame = channel.unary_unary(
        '/soc.protos.CatanServer/StartGame',
        request_serializer=catan__pb2.StartGameRequest.SerializeToString,
        response_deserializer=catan__pb2.StartGameResponse.FromString,
        )
    self.Subscribe = channel.unary_stream(
        '/soc.protos.CatanServer/Subscribe',
        request_serializer=catan__pb2.SubscribeRequest.SerializeToString,
        response_deserializer=catan__pb2.GameUpdate.FromString,
        )
    self.Move = channel.unary_unary(
        '/soc.protos.CatanServer/Move',
        request_serializer=catan__pb2.MoveRequest.SerializeToString,
        response_deserializer=catan__pb2.MoveResponse.FromString,
        )


class CatanServerServicer(object):
  """All RPCs must have a request and response message, even if empty
  """

  def CreateGame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartGame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Subscribe(self, request, context):
    """Subscribe to a game to recieve all its notifications
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CatanServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateGame': grpc.unary_unary_rpc_method_handler(
          servicer.CreateGame,
          request_deserializer=catan__pb2.CreateGameRequest.FromString,
          response_serializer=catan__pb2.CreateGameResponse.SerializeToString,
      ),
      'StartGame': grpc.unary_unary_rpc_method_handler(
          servicer.StartGame,
          request_deserializer=catan__pb2.StartGameRequest.FromString,
          response_serializer=catan__pb2.StartGameResponse.SerializeToString,
      ),
      'Subscribe': grpc.unary_stream_rpc_method_handler(
          servicer.Subscribe,
          request_deserializer=catan__pb2.SubscribeRequest.FromString,
          response_serializer=catan__pb2.GameUpdate.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=catan__pb2.MoveRequest.FromString,
          response_serializer=catan__pb2.MoveResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soc.protos.CatanServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
