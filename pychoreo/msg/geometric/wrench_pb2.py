# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geometric/wrench.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from primitive import header_pb2 as primitive_dot_header__pb2
from geometric import vector_pb2 as geometric_dot_vector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='geometric/wrench.proto',
  package='choreo',
  syntax='proto3',
  serialized_pb=_b('\n\x16geometric/wrench.proto\x12\x06\x63horeo\x1a\x16primitive/header.proto\x1a\x16geometric/vector.proto\"O\n\rWrenchStamped\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.choreo.Header\x12\x1e\n\x06wrench\x18\x02 \x01(\x0b\x32\x0e.choreo.Wrench\"I\n\x06Wrench\x12\x1e\n\x05\x66orce\x18\x01 \x01(\x0b\x32\x0f.choreo.Vector3\x12\x1f\n\x06torque\x18\x02 \x01(\x0b\x32\x0f.choreo.Vector3B1Z/github.com/RobotStudio/choreo-msg/msg/geometricb\x06proto3')
  ,
  dependencies=[primitive_dot_header__pb2.DESCRIPTOR,geometric_dot_vector__pb2.DESCRIPTOR,])




_WRENCHSTAMPED = _descriptor.Descriptor(
  name='WrenchStamped',
  full_name='choreo.WrenchStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='choreo.WrenchStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrench', full_name='choreo.WrenchStamped.wrench', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=161,
)


_WRENCH = _descriptor.Descriptor(
  name='Wrench',
  full_name='choreo.Wrench',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='force', full_name='choreo.Wrench.force', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='torque', full_name='choreo.Wrench.torque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=236,
)

_WRENCHSTAMPED.fields_by_name['header'].message_type = primitive_dot_header__pb2._HEADER
_WRENCHSTAMPED.fields_by_name['wrench'].message_type = _WRENCH
_WRENCH.fields_by_name['force'].message_type = geometric_dot_vector__pb2._VECTOR3
_WRENCH.fields_by_name['torque'].message_type = geometric_dot_vector__pb2._VECTOR3
DESCRIPTOR.message_types_by_name['WrenchStamped'] = _WRENCHSTAMPED
DESCRIPTOR.message_types_by_name['Wrench'] = _WRENCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WrenchStamped = _reflection.GeneratedProtocolMessageType('WrenchStamped', (_message.Message,), dict(
  DESCRIPTOR = _WRENCHSTAMPED,
  __module__ = 'geometric.wrench_pb2'
  # @@protoc_insertion_point(class_scope:choreo.WrenchStamped)
  ))
_sym_db.RegisterMessage(WrenchStamped)

Wrench = _reflection.GeneratedProtocolMessageType('Wrench', (_message.Message,), dict(
  DESCRIPTOR = _WRENCH,
  __module__ = 'geometric.wrench_pb2'
  # @@protoc_insertion_point(class_scope:choreo.Wrench)
  ))
_sym_db.RegisterMessage(Wrench)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z/github.com/RobotStudio/choreo-msg/msg/geometric'))
# @@protoc_insertion_point(module_scope)
