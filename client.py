import grpc
import greeting_pb2
import greeting_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
               
        name = input("Enter your name: ")
        response = stub.SayHello(greeting_pb2.HelloRequest(name=name))
        
    print(f"Server responded: {response.message}")

if __name__ == '__main__':
    run()