# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/peer_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import common_pb2 as candig_dot_schemas_dot_candig_dot_common__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/peer_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n(candig/schemas/candig/peer_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a\"candig/schemas/candig/common.proto\x1a+candig/schemas/google/api/annotations.proto\"9\n\x10ListPeersRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"X\n\x11ListPeersResponse\x12*\n\x05peers\x18\x01 \x03(\x0b\x32\x1b.candig.schemas.candig.Peer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"@\n\x13\x41nnouncePeerRequest\x12)\n\x04peer\x18\x01 \x01(\x0b\x32\x1b.candig.schemas.candig.Peer\"^\n\x14\x41nnouncePeerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.candig.schemas.candig.Attributes\"\x10\n\x0eGetInfoRequest\"b\n\x0fGetInfoResponse\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.candig.schemas.candig.Attributes\"J\n\x04Peer\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x35\n\nattributes\x18\x02 \x01(\x0b\x32!.candig.schemas.candig.Attributes2\x87\x03\n\x0bPeerService\x12\x80\x01\n\tListPeers\x12\'.candig.schemas.candig.ListPeersRequest\x1a(.candig.schemas.candig.ListPeersResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v0.6.0a10/peers/list:\x01*\x12\x84\x01\n\x0c\x41nnouncePeer\x12*.candig.schemas.candig.AnnouncePeerRequest\x1a+.candig.schemas.candig.AnnouncePeerResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/v0.6.0a10/announce\x12n\n\x04Info\x12%.candig.schemas.candig.GetInfoRequest\x1a&.candig.schemas.candig.GetInfoResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v0.6.0a10/infob\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_common__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LISTPEERSREQUEST = _descriptor.Descriptor(
  name='ListPeersRequest',
  full_name='candig.schemas.candig.ListPeersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.ListPeersRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.ListPeersRequest.page_token', index=1,
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
  serialized_start=148,
  serialized_end=205,
)


_LISTPEERSRESPONSE = _descriptor.Descriptor(
  name='ListPeersResponse',
  full_name='candig.schemas.candig.ListPeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='candig.schemas.candig.ListPeersResponse.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.ListPeersResponse.next_page_token', index=1,
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
  serialized_start=207,
  serialized_end=295,
)


_ANNOUNCEPEERREQUEST = _descriptor.Descriptor(
  name='AnnouncePeerRequest',
  full_name='candig.schemas.candig.AnnouncePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='candig.schemas.candig.AnnouncePeerRequest.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=297,
  serialized_end=361,
)


_ANNOUNCEPEERRESPONSE = _descriptor.Descriptor(
  name='AnnouncePeerResponse',
  full_name='candig.schemas.candig.AnnouncePeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='candig.schemas.candig.AnnouncePeerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.AnnouncePeerResponse.attributes', index=1,
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
  serialized_start=363,
  serialized_end=457,
)


_GETINFOREQUEST = _descriptor.Descriptor(
  name='GetInfoRequest',
  full_name='candig.schemas.candig.GetInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=459,
  serialized_end=475,
)


_GETINFORESPONSE = _descriptor.Descriptor(
  name='GetInfoResponse',
  full_name='candig.schemas.candig.GetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='candig.schemas.candig.GetInfoResponse.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.GetInfoResponse.attributes', index=1,
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
  serialized_start=477,
  serialized_end=575,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='candig.schemas.candig.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='candig.schemas.candig.Peer.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='candig.schemas.candig.Peer.attributes', index=1,
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
  serialized_start=577,
  serialized_end=651,
)

_LISTPEERSRESPONSE.fields_by_name['peers'].message_type = _PEER
_ANNOUNCEPEERREQUEST.fields_by_name['peer'].message_type = _PEER
_ANNOUNCEPEERRESPONSE.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
_GETINFORESPONSE.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
_PEER.fields_by_name['attributes'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ATTRIBUTES
DESCRIPTOR.message_types_by_name['ListPeersRequest'] = _LISTPEERSREQUEST
DESCRIPTOR.message_types_by_name['ListPeersResponse'] = _LISTPEERSRESPONSE
DESCRIPTOR.message_types_by_name['AnnouncePeerRequest'] = _ANNOUNCEPEERREQUEST
DESCRIPTOR.message_types_by_name['AnnouncePeerResponse'] = _ANNOUNCEPEERRESPONSE
DESCRIPTOR.message_types_by_name['GetInfoRequest'] = _GETINFOREQUEST
DESCRIPTOR.message_types_by_name['GetInfoResponse'] = _GETINFORESPONSE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPeersRequest = _reflection.GeneratedProtocolMessageType('ListPeersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSREQUEST,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.ListPeersRequest)
  ))
_sym_db.RegisterMessage(ListPeersRequest)

ListPeersResponse = _reflection.GeneratedProtocolMessageType('ListPeersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSRESPONSE,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.ListPeersResponse)
  ))
_sym_db.RegisterMessage(ListPeersResponse)

AnnouncePeerRequest = _reflection.GeneratedProtocolMessageType('AnnouncePeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANNOUNCEPEERREQUEST,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.AnnouncePeerRequest)
  ))
_sym_db.RegisterMessage(AnnouncePeerRequest)

AnnouncePeerResponse = _reflection.GeneratedProtocolMessageType('AnnouncePeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANNOUNCEPEERRESPONSE,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.AnnouncePeerResponse)
  ))
_sym_db.RegisterMessage(AnnouncePeerResponse)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINFOREQUEST,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetInfoRequest)
  ))
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINFORESPONSE,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetInfoResponse)
  ))
_sym_db.RegisterMessage(GetInfoResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(
  DESCRIPTOR = _PEER,
  __module__ = 'candig.schemas.candig.peer_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.Peer)
  ))
_sym_db.RegisterMessage(Peer)


# @@protoc_insertion_point(module_scope)