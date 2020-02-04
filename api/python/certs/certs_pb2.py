# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: certs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='certs.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\037com.zededa.cloud.uservice.protoZ#github.com/lf-edge/eve/api/go/certs'),
  serialized_pb=_b('\n\x0b\x63\x65rts.proto\":\n\rZEdgeNodeCert\x12\x12\n\ndeviceUuid\x18\x01 \x01(\t\x12\x15\n\x05\x63\x65rts\x18\x02 \x03(\x0b\x32\x06.ZCert\"(\n\x0fZControllerCert\x12\x15\n\x05\x63\x65rts\x18\x01 \x03(\x0b\x32\x06.ZCert\"e\n\x05ZCert\x12\x0e\n\x06\x63\x65rtId\x18\x01 \x01(\x0c\x12\x18\n\x04type\x18\x02 \x01(\x0e\x32\n.ZCertType\x12\x0c\n\x04\x63\x65rt\x18\x03 \x01(\x0c\x12$\n\nproperties\x18\x04 \x01(\x0b\x32\x10.ZCertProperties\"$\n\x0fZCertProperties\x12\x11\n\tisMutable\x18\x01 \x01(\x08*\xe9\x01\n\tZCertType\x12\x1f\n\x1b\x43\x45RT_TYPE_DEVICE_ONBOARDING\x10\x00\x12\'\n#CERT_TYPE_DEVICE_RESTRICTED_SIGNING\x10\x01\x12$\n CERT_TYPE_DEVICE_ENDORSEMENT_RSA\x10\x02\x12\"\n\x1e\x43\x45RT_TYPE_DEVICE_ECDH_EXCHANGE\x10\x03\x12 \n\x1c\x43\x45RT_TYPE_CONTROLLER_SIGNING\x10\x04\x12&\n\"CERT_TYPE_CONTROLLER_ECDH_EXCHANGE\x10\x05\x42\x46\n\x1f\x63om.zededa.cloud.uservice.protoZ#github.com/lf-edge/eve/api/go/certsb\x06proto3')
)

_ZCERTTYPE = _descriptor.EnumDescriptor(
  name='ZCertType',
  full_name='ZCertType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_DEVICE_ONBOARDING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_DEVICE_RESTRICTED_SIGNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_DEVICE_ENDORSEMENT_RSA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_DEVICE_ECDH_EXCHANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_CONTROLLER_SIGNING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CERT_TYPE_CONTROLLER_ECDH_EXCHANGE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=259,
  serialized_end=492,
)
_sym_db.RegisterEnumDescriptor(_ZCERTTYPE)

ZCertType = enum_type_wrapper.EnumTypeWrapper(_ZCERTTYPE)
CERT_TYPE_DEVICE_ONBOARDING = 0
CERT_TYPE_DEVICE_RESTRICTED_SIGNING = 1
CERT_TYPE_DEVICE_ENDORSEMENT_RSA = 2
CERT_TYPE_DEVICE_ECDH_EXCHANGE = 3
CERT_TYPE_CONTROLLER_SIGNING = 4
CERT_TYPE_CONTROLLER_ECDH_EXCHANGE = 5



_ZEDGENODECERT = _descriptor.Descriptor(
  name='ZEdgeNodeCert',
  full_name='ZEdgeNodeCert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceUuid', full_name='ZEdgeNodeCert.deviceUuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certs', full_name='ZEdgeNodeCert.certs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=73,
)


_ZCONTROLLERCERT = _descriptor.Descriptor(
  name='ZControllerCert',
  full_name='ZControllerCert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certs', full_name='ZControllerCert.certs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=115,
)


_ZCERT = _descriptor.Descriptor(
  name='ZCert',
  full_name='ZCert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certId', full_name='ZCert.certId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ZCert.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cert', full_name='ZCert.cert', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='ZCert.properties', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=218,
)


_ZCERTPROPERTIES = _descriptor.Descriptor(
  name='ZCertProperties',
  full_name='ZCertProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isMutable', full_name='ZCertProperties.isMutable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=256,
)

_ZEDGENODECERT.fields_by_name['certs'].message_type = _ZCERT
_ZCONTROLLERCERT.fields_by_name['certs'].message_type = _ZCERT
_ZCERT.fields_by_name['type'].enum_type = _ZCERTTYPE
_ZCERT.fields_by_name['properties'].message_type = _ZCERTPROPERTIES
DESCRIPTOR.message_types_by_name['ZEdgeNodeCert'] = _ZEDGENODECERT
DESCRIPTOR.message_types_by_name['ZControllerCert'] = _ZCONTROLLERCERT
DESCRIPTOR.message_types_by_name['ZCert'] = _ZCERT
DESCRIPTOR.message_types_by_name['ZCertProperties'] = _ZCERTPROPERTIES
DESCRIPTOR.enum_types_by_name['ZCertType'] = _ZCERTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZEdgeNodeCert = _reflection.GeneratedProtocolMessageType('ZEdgeNodeCert', (_message.Message,), dict(
  DESCRIPTOR = _ZEDGENODECERT,
  __module__ = 'certs_pb2'
  # @@protoc_insertion_point(class_scope:ZEdgeNodeCert)
  ))
_sym_db.RegisterMessage(ZEdgeNodeCert)

ZControllerCert = _reflection.GeneratedProtocolMessageType('ZControllerCert', (_message.Message,), dict(
  DESCRIPTOR = _ZCONTROLLERCERT,
  __module__ = 'certs_pb2'
  # @@protoc_insertion_point(class_scope:ZControllerCert)
  ))
_sym_db.RegisterMessage(ZControllerCert)

ZCert = _reflection.GeneratedProtocolMessageType('ZCert', (_message.Message,), dict(
  DESCRIPTOR = _ZCERT,
  __module__ = 'certs_pb2'
  # @@protoc_insertion_point(class_scope:ZCert)
  ))
_sym_db.RegisterMessage(ZCert)

ZCertProperties = _reflection.GeneratedProtocolMessageType('ZCertProperties', (_message.Message,), dict(
  DESCRIPTOR = _ZCERTPROPERTIES,
  __module__ = 'certs_pb2'
  # @@protoc_insertion_point(class_scope:ZCertProperties)
  ))
_sym_db.RegisterMessage(ZCertProperties)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)