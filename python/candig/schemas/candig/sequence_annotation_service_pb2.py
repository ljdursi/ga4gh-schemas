# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/sequence_annotation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import sequence_annotations_pb2 as candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/sequence_annotation_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n7candig/schemas/candig/sequence_annotation_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a\x30\x63\x61ndig/schemas/candig/sequence_annotations.proto\x1a+candig/schemas/google/api/annotations.proto\"U\n\x18SearchFeatureSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"m\n\x19SearchFeatureSetsResponse\x12\x37\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32!.candig.schemas.candig.FeatureSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\".\n\x14GetFeatureSetRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\"\xd7\x01\n\x15SearchFeaturesRequest\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x16\n\x0ereference_name\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x07 \x01(\x03\x12\x15\n\rfeature_types\x18\x08 \x03(\t\x12\x11\n\tpage_size\x18\t \x01(\x05\x12\x12\n\npage_token\x18\n \x01(\t\"c\n\x16SearchFeaturesResponse\x12\x30\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x1e.candig.schemas.candig.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\'\n\x11GetFeatureRequest\x12\x12\n\nfeature_id\x18\x01 \x01(\t\"X\n\x1bSearchContinuousSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"v\n\x1cSearchContinuousSetsResponse\x12=\n\x0f\x63ontinuous_sets\x18\x01 \x03(\x0b\x32$.candig.schemas.candig.ContinuousSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"4\n\x17GetContinuousSetRequest\x12\x19\n\x11\x63ontinuous_set_id\x18\x01 \x01(\t\"\x8f\x01\n\x17SearchContinuousRequest\x12\x19\n\x11\x63ontinuous_set_id\x18\x01 \x01(\t\x12\x16\n\x0ereference_name\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"j\n\x18SearchContinuousResponse\x12\x35\n\ncontinuous\x18\x01 \x03(\x0b\x32!.candig.schemas.candig.Continuous\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcb\x08\n\x19SequenceAnnotationService\x12\x9d\x01\n\x11SearchFeatureSets\x12/.candig.schemas.candig.SearchFeatureSetsRequest\x1a\x30.candig.schemas.candig.SearchFeatureSetsResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v0.8.0/featuresets/search:\x01*\x12\x8d\x01\n\rGetFeatureSet\x12+.candig.schemas.candig.GetFeatureSetRequest\x1a!.candig.schemas.candig.FeatureSet\",\x82\xd3\xe4\x93\x02&\x12$/v0.8.0/featuresets/{feature_set_id}\x12\x91\x01\n\x0eSearchFeatures\x12,.candig.schemas.candig.SearchFeaturesRequest\x1a-.candig.schemas.candig.SearchFeaturesResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v0.8.0/features/search:\x01*\x12}\n\nGetFeature\x12(.candig.schemas.candig.GetFeatureRequest\x1a\x1e.candig.schemas.candig.Feature\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v0.8.0/features/{feature_id}\x12\xab\x01\n\x14SearchContinuousSets\x12\x32.candig.schemas.candig.SearchContinuousSetsRequest\x1a\x33.candig.schemas.candig.SearchContinuousSetsResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v0.6.0a8/continuoussets/search:\x01*\x12\x9e\x01\n\x10GetContinuousSet\x12..candig.schemas.candig.GetContinuousSetRequest\x1a$.candig.schemas.candig.ContinuousSet\"4\x82\xd3\xe4\x93\x02.\x12,/v0.6.0a8/continuoussets/{continuous_set_id}\x12\x9b\x01\n\x10SearchContinuous\x12..candig.schemas.candig.SearchContinuousRequest\x1a/.candig.schemas.candig.SearchContinuousResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v0.6.0a8/continuous/search:\x01*b\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHFEATURESETSREQUEST = _descriptor.Descriptor(
  name='SearchFeatureSetsRequest',
  full_name='candig.schemas.candig.SearchFeatureSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.SearchFeatureSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchFeatureSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchFeatureSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=177,
  serialized_end=262,
)


_SEARCHFEATURESETSRESPONSE = _descriptor.Descriptor(
  name='SearchFeatureSetsResponse',
  full_name='candig.schemas.candig.SearchFeatureSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='candig.schemas.candig.SearchFeatureSetsResponse.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchFeatureSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=264,
  serialized_end=373,
)


_GETFEATURESETREQUEST = _descriptor.Descriptor(
  name='GetFeatureSetRequest',
  full_name='candig.schemas.candig.GetFeatureSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='candig.schemas.candig.GetFeatureSetRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=375,
  serialized_end=421,
)


_SEARCHFEATURESREQUEST = _descriptor.Descriptor(
  name='SearchFeaturesRequest',
  full_name='candig.schemas.candig.SearchFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='candig.schemas.candig.SearchFeaturesRequest.feature_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.SearchFeaturesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='candig.schemas.candig.SearchFeaturesRequest.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='candig.schemas.candig.SearchFeaturesRequest.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='candig.schemas.candig.SearchFeaturesRequest.reference_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='candig.schemas.candig.SearchFeaturesRequest.start', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='candig.schemas.candig.SearchFeaturesRequest.end', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_types', full_name='candig.schemas.candig.SearchFeaturesRequest.feature_types', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchFeaturesRequest.page_size', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchFeaturesRequest.page_token', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=424,
  serialized_end=639,
)


_SEARCHFEATURESRESPONSE = _descriptor.Descriptor(
  name='SearchFeaturesResponse',
  full_name='candig.schemas.candig.SearchFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='candig.schemas.candig.SearchFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchFeaturesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=641,
  serialized_end=740,
)


_GETFEATUREREQUEST = _descriptor.Descriptor(
  name='GetFeatureRequest',
  full_name='candig.schemas.candig.GetFeatureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='candig.schemas.candig.GetFeatureRequest.feature_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=742,
  serialized_end=781,
)


_SEARCHCONTINUOUSSETSREQUEST = _descriptor.Descriptor(
  name='SearchContinuousSetsRequest',
  full_name='candig.schemas.candig.SearchContinuousSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.SearchContinuousSetsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchContinuousSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchContinuousSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=783,
  serialized_end=871,
)


_SEARCHCONTINUOUSSETSRESPONSE = _descriptor.Descriptor(
  name='SearchContinuousSetsResponse',
  full_name='candig.schemas.candig.SearchContinuousSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='continuous_sets', full_name='candig.schemas.candig.SearchContinuousSetsResponse.continuous_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchContinuousSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=873,
  serialized_end=991,
)


_GETCONTINUOUSSETREQUEST = _descriptor.Descriptor(
  name='GetContinuousSetRequest',
  full_name='candig.schemas.candig.GetContinuousSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='continuous_set_id', full_name='candig.schemas.candig.GetContinuousSetRequest.continuous_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=993,
  serialized_end=1045,
)


_SEARCHCONTINUOUSREQUEST = _descriptor.Descriptor(
  name='SearchContinuousRequest',
  full_name='candig.schemas.candig.SearchContinuousRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='continuous_set_id', full_name='candig.schemas.candig.SearchContinuousRequest.continuous_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='candig.schemas.candig.SearchContinuousRequest.reference_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='candig.schemas.candig.SearchContinuousRequest.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='candig.schemas.candig.SearchContinuousRequest.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchContinuousRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchContinuousRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1048,
  serialized_end=1191,
)


_SEARCHCONTINUOUSRESPONSE = _descriptor.Descriptor(
  name='SearchContinuousResponse',
  full_name='candig.schemas.candig.SearchContinuousResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='continuous', full_name='candig.schemas.candig.SearchContinuousResponse.continuous', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchContinuousResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1193,
  serialized_end=1299,
)

_SEARCHFEATURESETSRESPONSE.fields_by_name['feature_sets'].message_type = candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2._FEATURESET
_SEARCHFEATURESRESPONSE.fields_by_name['features'].message_type = candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2._FEATURE
_SEARCHCONTINUOUSSETSRESPONSE.fields_by_name['continuous_sets'].message_type = candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2._CONTINUOUSSET
_SEARCHCONTINUOUSRESPONSE.fields_by_name['continuous'].message_type = candig_dot_schemas_dot_candig_dot_sequence__annotations__pb2._CONTINUOUS
DESCRIPTOR.message_types_by_name['SearchFeatureSetsRequest'] = _SEARCHFEATURESETSREQUEST
DESCRIPTOR.message_types_by_name['SearchFeatureSetsResponse'] = _SEARCHFEATURESETSRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureSetRequest'] = _GETFEATURESETREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesRequest'] = _SEARCHFEATURESREQUEST
DESCRIPTOR.message_types_by_name['SearchFeaturesResponse'] = _SEARCHFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetFeatureRequest'] = _GETFEATUREREQUEST
DESCRIPTOR.message_types_by_name['SearchContinuousSetsRequest'] = _SEARCHCONTINUOUSSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchContinuousSetsResponse'] = _SEARCHCONTINUOUSSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetContinuousSetRequest'] = _GETCONTINUOUSSETREQUEST
DESCRIPTOR.message_types_by_name['SearchContinuousRequest'] = _SEARCHCONTINUOUSREQUEST
DESCRIPTOR.message_types_by_name['SearchContinuousResponse'] = _SEARCHCONTINUOUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchFeatureSetsRequest = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchFeatureSetsRequest)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsRequest)

SearchFeatureSetsResponse = _reflection.GeneratedProtocolMessageType('SearchFeatureSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESETSRESPONSE,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchFeatureSetsResponse)
  ))
_sym_db.RegisterMessage(SearchFeatureSetsResponse)

GetFeatureSetRequest = _reflection.GeneratedProtocolMessageType('GetFeatureSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATURESETREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetFeatureSetRequest)
  ))
_sym_db.RegisterMessage(GetFeatureSetRequest)

SearchFeaturesRequest = _reflection.GeneratedProtocolMessageType('SearchFeaturesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchFeaturesRequest)
  ))
_sym_db.RegisterMessage(SearchFeaturesRequest)

SearchFeaturesResponse = _reflection.GeneratedProtocolMessageType('SearchFeaturesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHFEATURESRESPONSE,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchFeaturesResponse)
  ))
_sym_db.RegisterMessage(SearchFeaturesResponse)

GetFeatureRequest = _reflection.GeneratedProtocolMessageType('GetFeatureRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATUREREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetFeatureRequest)
  ))
_sym_db.RegisterMessage(GetFeatureRequest)

SearchContinuousSetsRequest = _reflection.GeneratedProtocolMessageType('SearchContinuousSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCONTINUOUSSETSREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchContinuousSetsRequest)
  ))
_sym_db.RegisterMessage(SearchContinuousSetsRequest)

SearchContinuousSetsResponse = _reflection.GeneratedProtocolMessageType('SearchContinuousSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCONTINUOUSSETSRESPONSE,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchContinuousSetsResponse)
  ))
_sym_db.RegisterMessage(SearchContinuousSetsResponse)

GetContinuousSetRequest = _reflection.GeneratedProtocolMessageType('GetContinuousSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONTINUOUSSETREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetContinuousSetRequest)
  ))
_sym_db.RegisterMessage(GetContinuousSetRequest)

SearchContinuousRequest = _reflection.GeneratedProtocolMessageType('SearchContinuousRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCONTINUOUSREQUEST,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchContinuousRequest)
  ))
_sym_db.RegisterMessage(SearchContinuousRequest)

SearchContinuousResponse = _reflection.GeneratedProtocolMessageType('SearchContinuousResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHCONTINUOUSRESPONSE,
  __module__ = 'candig.schemas.candig.sequence_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchContinuousResponse)
  ))
_sym_db.RegisterMessage(SearchContinuousResponse)


# @@protoc_insertion_point(module_scope)
