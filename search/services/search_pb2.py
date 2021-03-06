# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from structures import region_pb2 as structures_dot_region__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/search.proto',
  package='gcv.services',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15services/search.proto\x12\x0cgcv.services\x1a\x17structures/region.proto\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"E\n\x0bSearchReply\x12\r\n\x05genes\x18\x01 \x03(\t\x12\'\n\x07regions\x18\x02 \x03(\x0b\x32\x16.gcv.structures.Region2L\n\x06Search\x12\x42\n\x06Search\x12\x1b.gcv.services.SearchRequest\x1a\x19.gcv.services.SearchReply\"\x00\x62\x06proto3'
  ,
  dependencies=[structures_dot_region__pb2.DESCRIPTOR,])




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='gcv.services.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='gcv.services.SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=94,
)


_SEARCHREPLY = _descriptor.Descriptor(
  name='SearchReply',
  full_name='gcv.services.SearchReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genes', full_name='gcv.services.SearchReply.genes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regions', full_name='gcv.services.SearchReply.regions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=96,
  serialized_end=165,
)

_SEARCHREPLY.fields_by_name['regions'].message_type = structures_dot_region__pb2._REGION
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchReply'] = _SEARCHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'services.search_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchReply = _reflection.GeneratedProtocolMessageType('SearchReply', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREPLY,
  '__module__' : 'services.search_pb2'
  # @@protoc_insertion_point(class_scope:gcv.services.SearchReply)
  })
_sym_db.RegisterMessage(SearchReply)



_SEARCH = _descriptor.ServiceDescriptor(
  name='Search',
  full_name='gcv.services.Search',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=243,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='gcv.services.Search.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCH)

DESCRIPTOR.services_by_name['Search'] = _SEARCH

# @@protoc_insertion_point(module_scope)
