from core import topology_pb2 as _topology_pb2
from core import filters_pb2 as _filters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LsLinkEvent(_message.Message):
    __slots__ = ["action", "key", "ls_link"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LS_LINK_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    ls_link: _topology_pb2.LsLink
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., ls_link: _Optional[_Union[_topology_pb2.LsLink, _Mapping]] = ...) -> None: ...

class LsNodeEdgeEvent(_message.Message):
    __slots__ = ["action", "key", "ls_node_edge"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LS_NODE_EDGE_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    ls_node_edge: _topology_pb2.LsNodeEdge
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., ls_node_edge: _Optional[_Union[_topology_pb2.LsNodeEdge, _Mapping]] = ...) -> None: ...

class LsNodeEvent(_message.Message):
    __slots__ = ["action", "key", "ls_node"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LS_NODE_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    ls_node: _topology_pb2.LsNode
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., ls_node: _Optional[_Union[_topology_pb2.LsNode, _Mapping]] = ...) -> None: ...

class LsPrefixEvent(_message.Message):
    __slots__ = ["action", "key", "ls_prefix"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    ls_prefix: _topology_pb2.LsPrefix
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., ls_prefix: _Optional[_Union[_topology_pb2.LsPrefix, _Mapping]] = ...) -> None: ...

class LsSrv6SidEvent(_message.Message):
    __slots__ = ["action", "key", "ls_srv6_sid"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LS_SRV6_SID_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    ls_srv6_sid: _topology_pb2.LsSrv6Sid
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., ls_srv6_sid: _Optional[_Union[_topology_pb2.LsSrv6Sid, _Mapping]] = ...) -> None: ...

class PeerEvent(_message.Message):
    __slots__ = ["action", "key", "peer"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PEER_FIELD_NUMBER: _ClassVar[int]
    action: str
    key: str
    peer: _topology_pb2.Peer
    def __init__(self, action: _Optional[str] = ..., key: _Optional[str] = ..., peer: _Optional[_Union[_topology_pb2.Peer, _Mapping]] = ...) -> None: ...

class TelemetryEvent(_message.Message):
    __slots__ = ["telemetry_data"]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    telemetry_data: str
    def __init__(self, telemetry_data: _Optional[str] = ...) -> None: ...

class TelemetrySubscription(_message.Message):
    __slots__ = ["Unflatten", "properties", "sensor_path", "string_filters"]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SENSOR_PATH_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTERS_FIELD_NUMBER: _ClassVar[int]
    UNFLATTEN_FIELD_NUMBER: _ClassVar[int]
    Unflatten: bool
    properties: _containers.RepeatedScalarFieldContainer[str]
    sensor_path: str
    string_filters: _containers.RepeatedCompositeFieldContainer[_filters_pb2.StringFilter]
    def __init__(self, sensor_path: _Optional[str] = ..., properties: _Optional[_Iterable[str]] = ..., Unflatten: bool = ..., string_filters: _Optional[_Iterable[_Union[_filters_pb2.StringFilter, _Mapping]]] = ...) -> None: ...

class TopologySubscription(_message.Message):
    __slots__ = ["keys", "properties"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., properties: _Optional[_Iterable[str]] = ...) -> None: ...
