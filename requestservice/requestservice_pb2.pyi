from core import topology_pb2 as _topology_pb2
from core import filters_pb2 as _filters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LsLinkResponse(_message.Message):
    __slots__ = ["ls_links"]
    LS_LINKS_FIELD_NUMBER: _ClassVar[int]
    ls_links: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsLink]
    def __init__(self, ls_links: _Optional[_Iterable[_Union[_topology_pb2.LsLink, _Mapping]]] = ...) -> None: ...

class LsNodeCoordinatesRequest(_message.Message):
    __slots__ = ["ls_node_keys"]
    LS_NODE_KEYS_FIELD_NUMBER: _ClassVar[int]
    ls_node_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ls_node_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class LsNodeCoordinatesResponse(_message.Message):
    __slots__ = ["coordinates"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsNodeCoordinates]
    def __init__(self, coordinates: _Optional[_Iterable[_Union[_topology_pb2.LsNodeCoordinates, _Mapping]]] = ...) -> None: ...

class LsNodeEdgeResponse(_message.Message):
    __slots__ = ["ls_node_edges"]
    LS_NODE_EDGES_FIELD_NUMBER: _ClassVar[int]
    ls_node_edges: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsNodeEdge]
    def __init__(self, ls_node_edges: _Optional[_Iterable[_Union[_topology_pb2.LsNodeEdge, _Mapping]]] = ...) -> None: ...

class LsNodeResponse(_message.Message):
    __slots__ = ["ls_nodes"]
    LS_NODES_FIELD_NUMBER: _ClassVar[int]
    ls_nodes: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsNode]
    def __init__(self, ls_nodes: _Optional[_Iterable[_Union[_topology_pb2.LsNode, _Mapping]]] = ...) -> None: ...

class LsPrefixResponse(_message.Message):
    __slots__ = ["ls_prefixes"]
    LS_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    ls_prefixes: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsPrefix]
    def __init__(self, ls_prefixes: _Optional[_Iterable[_Union[_topology_pb2.LsPrefix, _Mapping]]] = ...) -> None: ...

class LsSrv6SidResponse(_message.Message):
    __slots__ = ["ls_srv6_sids"]
    LS_SRV6_SIDS_FIELD_NUMBER: _ClassVar[int]
    ls_srv6_sids: _containers.RepeatedCompositeFieldContainer[_topology_pb2.LsSrv6Sid]
    def __init__(self, ls_srv6_sids: _Optional[_Iterable[_Union[_topology_pb2.LsSrv6Sid, _Mapping]]] = ...) -> None: ...

class Measurement(_message.Message):
    __slots__ = ["name", "timestamp_latest_measurement"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_LATEST_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    timestamp_latest_measurement: int
    def __init__(self, name: _Optional[str] = ..., timestamp_latest_measurement: _Optional[int] = ...) -> None: ...

class MeasurementColumn(_message.Message):
    __slots__ = ["influx_type", "last_value_stringyfied", "name", "type"]
    INFLUX_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_VALUE_STRINGYFIED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    influx_type: str
    last_value_stringyfied: str
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., influx_type: _Optional[str] = ..., last_value_stringyfied: _Optional[str] = ...) -> None: ...

class MeasurementDetailsRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MeasurementDetailsResponse(_message.Message):
    __slots__ = ["columns", "timestamp_latest_measurement"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_LATEST_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[MeasurementColumn]
    timestamp_latest_measurement: int
    def __init__(self, timestamp_latest_measurement: _Optional[int] = ..., columns: _Optional[_Iterable[_Union[MeasurementColumn, _Mapping]]] = ...) -> None: ...

class MeasurementsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MeasurementsResponse(_message.Message):
    __slots__ = ["measurements"]
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    measurements: _containers.RepeatedCompositeFieldContainer[Measurement]
    def __init__(self, measurements: _Optional[_Iterable[_Union[Measurement, _Mapping]]] = ...) -> None: ...

class PeerResponse(_message.Message):
    __slots__ = ["peer"]
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _containers.RepeatedCompositeFieldContainer[_topology_pb2.Peer]
    def __init__(self, peer: _Optional[_Iterable[_Union[_topology_pb2.Peer, _Mapping]]] = ...) -> None: ...

class TelemetryRequest(_message.Message):
    __slots__ = ["Unflatten", "properties", "range_filter", "sensor_path", "string_filters"]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RANGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SENSOR_PATH_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTERS_FIELD_NUMBER: _ClassVar[int]
    UNFLATTEN_FIELD_NUMBER: _ClassVar[int]
    Unflatten: bool
    properties: _containers.RepeatedScalarFieldContainer[str]
    range_filter: _filters_pb2.RangeFilter
    sensor_path: str
    string_filters: _containers.RepeatedCompositeFieldContainer[_filters_pb2.StringFilter]
    def __init__(self, sensor_path: _Optional[str] = ..., properties: _Optional[_Iterable[str]] = ..., Unflatten: bool = ..., string_filters: _Optional[_Iterable[_Union[_filters_pb2.StringFilter, _Mapping]]] = ..., range_filter: _Optional[_Union[_filters_pb2.RangeFilter, _Mapping]] = ...) -> None: ...

class TelemetryResponse(_message.Message):
    __slots__ = ["telemetry_data"]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    telemetry_data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, telemetry_data: _Optional[_Iterable[str]] = ...) -> None: ...

class TopologyRequest(_message.Message):
    __slots__ = ["keys", "properties"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., properties: _Optional[_Iterable[str]] = ...) -> None: ...
