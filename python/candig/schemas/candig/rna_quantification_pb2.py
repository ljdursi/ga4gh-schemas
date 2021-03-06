# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/rna_quantification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import common_pb2 as candig_dot_schemas_dot_candig_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/rna_quantification.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n.candig/schemas/candig/rna_quantification.proto\x12\x15\x63\x61ndig.schemas.candig\x1a\"candig/schemas/candig/common.proto\"{\n\x14RnaQuantificationSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x35\n\nattributes\x18\x04 \x01(\x0b\x32!.candig.schemas.candig.Attributes\"\xba\x02\n\x11RnaQuantification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0eread_group_ids\x18\x04 \x03(\t\x12\x30\n\x08programs\x18\x05 \x03(\x0b\x32\x1e.candig.schemas.candig.Program\x12\x17\n\x0f\x66\x65\x61ture_set_ids\x18\x06 \x03(\t\x12!\n\x19rna_quantification_set_id\x18\x07 \x01(\t\x12\x35\n\nattributes\x18\t \x01(\x0b\x32!.candig.schemas.candig.Attributes\x12\x10\n\x08sampleId\x18\n \x01(\t\x12\x11\n\tpatientId\x18\x0b \x01(\t\"\xc0\x02\n\x0f\x45xpressionLevel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x15rna_quantification_id\x18\x04 \x01(\t\x12\x16\n\x0eraw_read_count\x18\x05 \x01(\x02\x12\x12\n\nexpression\x18\x06 \x01(\x02\x12\x15\n\ris_normalized\x18\x07 \x01(\x08\x12\x34\n\x05units\x18\x08 \x01(\x0e\x32%.candig.schemas.candig.ExpressionUnit\x12\r\n\x05score\x18\t \x01(\x02\x12\x19\n\x11\x63onf_interval_low\x18\n \x01(\x02\x12\x1a\n\x12\x63onf_interval_high\x18\x0b \x01(\x02\x12\x35\n\nattributes\x18\x0c \x01(\x0b\x32!.candig.schemas.candig.Attributes*N\n\x0e\x45xpressionUnit\x12\x1f\n\x1b\x45XPRESSION_UNIT_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46PKM\x10\x01\x12\x07\n\x03TPM\x10\x02\x12\x08\n\x04RPKM\x10\x03\x62\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_common__pb2.DESCRIPTOR,])

_EXPRESSIONUNIT = _descriptor.EnumDescriptor(
  name='ExpressionUnit',
  full_name='candig.schemas.candig.ExpressionUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPRESSION_UNIT_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FPKM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPKM', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=874,
  serialized_end=952,
)
_sym_db.RegisterEnumDescriptor(_EXPRESSIONUNIT)

ExpressionUnit = enum_type_wrapper.EnumTypeWrapper(_EXPRESSIONUNIT)
EXPRESSION_UNIT_UNSPECIFIED = 0
FPKM = 1
TPM = 2
RPKM = 3



_RNAQUANTIFICATIONSET = _descriptor.Descriptor(
  name='RnaQuantificationSet',
  full_name='candig.schemas.candig.RnaQuantificationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='candig.schemas.candig.RnaQuantificationSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.RnaQuantificationSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.RnaQuantificationSet.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.RnaQuantificationSet.attributes', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=109,
  serialized_end=232,
)


_RNAQUANTIFICATION = _descriptor.Descriptor(
  name='RnaQuantification',
  full_name='candig.schemas.candig.RnaQuantification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='candig.schemas.candig.RnaQuantification.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.RnaQuantification.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='candig.schemas.candig.RnaQuantification.biosample_id', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='candig.schemas.candig.RnaQuantification.description', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_group_ids', full_name='candig.schemas.candig.RnaQuantification.read_group_ids', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='programs', full_name='candig.schemas.candig.RnaQuantification.programs', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_set_ids', full_name='candig.schemas.candig.RnaQuantification.feature_set_ids', index=6,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rna_quantification_set_id', full_name='candig.schemas.candig.RnaQuantification.rna_quantification_set_id', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.RnaQuantification.attributes', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sampleId', full_name='candig.schemas.candig.RnaQuantification.sampleId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patientId', full_name='candig.schemas.candig.RnaQuantification.patientId', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=235,
  serialized_end=549,
)


_EXPRESSIONLEVEL = _descriptor.Descriptor(
  name='ExpressionLevel',
  full_name='candig.schemas.candig.ExpressionLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='candig.schemas.candig.ExpressionLevel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.ExpressionLevel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rna_quantification_id', full_name='candig.schemas.candig.ExpressionLevel.rna_quantification_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_read_count', full_name='candig.schemas.candig.ExpressionLevel.raw_read_count', index=3,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expression', full_name='candig.schemas.candig.ExpressionLevel.expression', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_normalized', full_name='candig.schemas.candig.ExpressionLevel.is_normalized', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='candig.schemas.candig.ExpressionLevel.units', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='candig.schemas.candig.ExpressionLevel.score', index=7,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conf_interval_low', full_name='candig.schemas.candig.ExpressionLevel.conf_interval_low', index=8,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conf_interval_high', full_name='candig.schemas.candig.ExpressionLevel.conf_interval_high', index=9,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.ExpressionLevel.attributes', index=10,
      number=12, type=11, cpp_type=10, label=1,
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
  serialized_start=552,
  serialized_end=872,
)

_RNAQUANTIFICATIONSET.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
_RNAQUANTIFICATION.fields_by_name['programs'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._PROGRAM
_RNAQUANTIFICATION.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
_EXPRESSIONLEVEL.fields_by_name['units'].enum_type = _EXPRESSIONUNIT
_EXPRESSIONLEVEL.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
DESCRIPTOR.message_types_by_name['RnaQuantificationSet'] = _RNAQUANTIFICATIONSET
DESCRIPTOR.message_types_by_name['RnaQuantification'] = _RNAQUANTIFICATION
DESCRIPTOR.message_types_by_name['ExpressionLevel'] = _EXPRESSIONLEVEL
DESCRIPTOR.enum_types_by_name['ExpressionUnit'] = _EXPRESSIONUNIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RnaQuantificationSet = _reflection.GeneratedProtocolMessageType('RnaQuantificationSet', (_message.Message,), dict(
  DESCRIPTOR = _RNAQUANTIFICATIONSET,
  __module__ = 'candig.schemas.candig.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.RnaQuantificationSet)
  ))
_sym_db.RegisterMessage(RnaQuantificationSet)

RnaQuantification = _reflection.GeneratedProtocolMessageType('RnaQuantification', (_message.Message,), dict(
  DESCRIPTOR = _RNAQUANTIFICATION,
  __module__ = 'candig.schemas.candig.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.RnaQuantification)
  ))
_sym_db.RegisterMessage(RnaQuantification)

ExpressionLevel = _reflection.GeneratedProtocolMessageType('ExpressionLevel', (_message.Message,), dict(
  DESCRIPTOR = _EXPRESSIONLEVEL,
  __module__ = 'candig.schemas.candig.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.ExpressionLevel)
  ))
_sym_db.RegisterMessage(ExpressionLevel)


# @@protoc_insertion_point(module_scope)
