import grpc

import hello_pb2_grpc
import hello_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.GreeterStub(channel)


request = hello_pb2.HelloRequest(name='Dani')
response = stub.SayHello(request)
print("Greeting: " + str(response.message))
