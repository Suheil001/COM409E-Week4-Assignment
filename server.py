from concurrent import futures
import grpc
import greeting_pb2
import greeting_pb2_grpc

class Greeter(greeting_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Received request from: {request.name}")
        return greeting_pb2.HelloReply(message=f'Hello, {request.name}! Welcome to Distributed Systems.')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()