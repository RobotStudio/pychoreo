"""Echo GRPC Service"""

import time
from concurrent import futures

import grpc

from pychoreo import svc


class Echo(svc.echo_pb2_grpc.EchoServicer):
    def echo(self, request, context):
        return svc.echo_pb2.Echo(data=request.data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    svc.echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
