# django_client/greet_app/views.py

from django.http import JsonResponse
import grpc
from .proto import greet_pb2
from .proto import greet_pb2_grpc


def hello_view(request):
    name = request.GET.get("name", "World")

    # Connect to gRPC server
    with grpc.insecure_channel("go-service.internal.golang-django-hello.local:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greet_pb2.HelloRequest(name=name))

    return JsonResponse({"message": response.message})
