from core import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeFilter(_message.Message):
    __slots__ = ["earliest_timestamp", "latest_timestamp"]
    EARLIEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    earliest_timestamp: int
    latest_timestamp: int
    def __init__(self, earliest_timestamp: _Optional[int] = ..., latest_timestamp: _Optional[int] = ...) -> None: ...

class StringFilter(_message.Message):
    __slots__ = ["operator", "property", "value"]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operator: _enums_pb2.StringOperator
    property: str
    value: str
    def __init__(self, property: _Optional[str] = ..., value: _Optional[str] = ..., operator: _Optional[_Union[_enums_pb2.StringOperator, str]] = ...) -> None: ...
