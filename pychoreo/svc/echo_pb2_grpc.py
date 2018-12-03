# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from msg.primitive import string_pb2 as msg_dot_primitive_dot_string__pb2


class EchoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/choreo.Echo/Echo',
        request_serializer=msg_dot_primitive_dot_string__pb2.String.SerializeToString,
        response_deserializer=msg_dot_primitive_dot_string__pb2.String.FromString,
        )


class EchoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=msg_dot_primitive_dot_string__pb2.String.FromString,
          response_serializer=msg_dot_primitive_dot_string__pb2.String.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'choreo.Echo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
