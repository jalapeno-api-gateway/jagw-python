# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/filters.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from core import enums_pb2 as core_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63ore/filters.proto\x12\x04jagw\x1a\x10\x63ore/enums.proto\"W\n\x0cStringFilter\x12\x10\n\x08property\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12&\n\x08operator\x18\x03 \x02(\x0e\x32\x14.jagw.StringOperator\"C\n\x0bRangeFilter\x12\x1a\n\x12\x65\x61rliest_timestamp\x18\x03 \x02(\x03\x12\x18\n\x10latest_timestamp\x18\x04 \x01(\x03\x42.Z,github.com/jalapeno-api-gateway/jagw-go;jagw')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.filters_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/jalapeno-api-gateway/jagw-go;jagw'
  _STRINGFILTER._serialized_start=46
  _STRINGFILTER._serialized_end=133
  _RANGEFILTER._serialized_start=135
  _RANGEFILTER._serialized_end=202
# @@protoc_insertion_point(module_scope)
