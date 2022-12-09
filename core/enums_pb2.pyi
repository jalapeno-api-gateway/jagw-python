from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
EQUAL: StringOperator
NOT_EQUAL: StringOperator

class StringOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
