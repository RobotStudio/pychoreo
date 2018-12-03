"""Echo GRPC Service"""

import time
from concurrent import futures

import grpc

from pychoreo.svc import echo_pb2, echo_pb2_grpc


class Echo(echo_pb2_grpc.EchoServicer):
    def echo(self, request, context):
        return echo_pb2.Echo(data=request.data)


def echo_srv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    srv()
