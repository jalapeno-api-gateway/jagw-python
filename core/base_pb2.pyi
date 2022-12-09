from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MultiTopologyIdentifier(_message.Message):
    __slots__ = ["a_flag", "mtid", "o_flag"]
    A_FLAG_FIELD_NUMBER: _ClassVar[int]
    MTID_FIELD_NUMBER: _ClassVar[int]
    O_FLAG_FIELD_NUMBER: _ClassVar[int]
    a_flag: bool
    mtid: int
    o_flag: bool
    def __init__(self, o_flag: bool = ..., a_flag: bool = ..., mtid: _Optional[int] = ...) -> None: ...
