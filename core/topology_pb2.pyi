from core import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LsLink(_message.Message):
    __slots__ = ["area_id", "domain_id", "id", "igp_metric", "igp_router_id", "key", "local_link_id", "local_link_ip", "local_node_hash", "mtid", "nexthop", "peer_asn", "peer_hash", "peer_ip", "protocol", "remote_igp_router_id", "remote_link_id", "remote_link_ip", "remote_node_hash", "router_hash", "router_ip", "timestamp"]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IGP_METRIC_FIELD_NUMBER: _ClassVar[int]
    IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LINK_IP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NODE_HASH_FIELD_NUMBER: _ClassVar[int]
    MTID_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_HASH_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REMOTE_IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_LINK_IP_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NODE_HASH_FIELD_NUMBER: _ClassVar[int]
    ROUTER_HASH_FIELD_NUMBER: _ClassVar[int]
    ROUTER_IP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    area_id: str
    domain_id: int
    id: str
    igp_metric: int
    igp_router_id: str
    key: str
    local_link_id: str
    local_link_ip: str
    local_node_hash: str
    mtid: _base_pb2.MultiTopologyIdentifier
    nexthop: str
    peer_asn: int
    peer_hash: str
    peer_ip: str
    protocol: str
    remote_igp_router_id: str
    remote_link_id: str
    remote_link_ip: str
    remote_node_hash: str
    router_hash: str
    router_ip: str
    timestamp: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., router_hash: _Optional[str] = ..., router_ip: _Optional[str] = ..., domain_id: _Optional[int] = ..., peer_hash: _Optional[str] = ..., peer_ip: _Optional[str] = ..., peer_asn: _Optional[int] = ..., timestamp: _Optional[str] = ..., igp_router_id: _Optional[str] = ..., protocol: _Optional[str] = ..., area_id: _Optional[str] = ..., nexthop: _Optional[str] = ..., mtid: _Optional[_Union[_base_pb2.MultiTopologyIdentifier, _Mapping]] = ..., local_link_id: _Optional[str] = ..., remote_link_id: _Optional[str] = ..., local_link_ip: _Optional[str] = ..., remote_link_ip: _Optional[str] = ..., igp_metric: _Optional[int] = ..., remote_node_hash: _Optional[str] = ..., local_node_hash: _Optional[str] = ..., remote_igp_router_id: _Optional[str] = ...) -> None: ...

class LsNode(_message.Message):
    __slots__ = ["area_id", "asn", "domain_id", "id", "igp_router_id", "is_adj_rib_in", "is_prepolicy", "key", "mtid", "name", "peer_asn", "peer_hash", "peer_ip", "protocol", "protocol_id", "router_hash", "router_ip", "timestamp"]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    ASN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADJ_RIB_IN_FIELD_NUMBER: _ClassVar[int]
    IS_PREPOLICY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_HASH_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTER_HASH_FIELD_NUMBER: _ClassVar[int]
    ROUTER_IP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    area_id: str
    asn: int
    domain_id: int
    id: str
    igp_router_id: str
    is_adj_rib_in: bool
    is_prepolicy: bool
    key: str
    mtid: _containers.RepeatedCompositeFieldContainer[_base_pb2.MultiTopologyIdentifier]
    name: str
    peer_asn: int
    peer_hash: str
    peer_ip: str
    protocol: str
    protocol_id: int
    router_hash: str
    router_ip: str
    timestamp: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., router_hash: _Optional[str] = ..., domain_id: _Optional[int] = ..., router_ip: _Optional[str] = ..., peer_hash: _Optional[str] = ..., peer_ip: _Optional[str] = ..., peer_asn: _Optional[int] = ..., timestamp: _Optional[str] = ..., igp_router_id: _Optional[str] = ..., asn: _Optional[int] = ..., mtid: _Optional[_Iterable[_Union[_base_pb2.MultiTopologyIdentifier, _Mapping]]] = ..., area_id: _Optional[str] = ..., protocol: _Optional[str] = ..., protocol_id: _Optional[int] = ..., name: _Optional[str] = ..., is_prepolicy: bool = ..., is_adj_rib_in: bool = ...) -> None: ...

class LsNodeCoordinates(_message.Message):
    __slots__ = ["id", "key", "latitude", "longitude", "ls_node_key"]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    LS_NODE_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    latitude: float
    longitude: float
    ls_node_key: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., ls_node_key: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class LsNodeEdge(_message.Message):
    __slots__ = ["id", "key", "link", "to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    link: str
    to: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., to: _Optional[str] = ..., link: _Optional[str] = ..., **kwargs) -> None: ...

class LsPrefix(_message.Message):
    __slots__ = ["area_id", "domain_id", "id", "igp_router_id", "is_adj_rib_in", "is_prepolicy", "key", "local_node_hash", "mtid", "nexthop", "peer_asn", "peer_hash", "peer_ip", "prefix", "prefix_len", "prefix_metric", "protocol", "router_hash", "router_ip", "timestamp"]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADJ_RIB_IN_FIELD_NUMBER: _ClassVar[int]
    IS_PREPOLICY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NODE_HASH_FIELD_NUMBER: _ClassVar[int]
    MTID_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_HASH_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_METRIC_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_HASH_FIELD_NUMBER: _ClassVar[int]
    ROUTER_IP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    area_id: str
    domain_id: int
    id: str
    igp_router_id: str
    is_adj_rib_in: bool
    is_prepolicy: bool
    key: str
    local_node_hash: str
    mtid: _base_pb2.MultiTopologyIdentifier
    nexthop: str
    peer_asn: int
    peer_hash: str
    peer_ip: str
    prefix: str
    prefix_len: int
    prefix_metric: int
    protocol: str
    router_hash: str
    router_ip: str
    timestamp: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., router_hash: _Optional[str] = ..., router_ip: _Optional[str] = ..., domain_id: _Optional[int] = ..., peer_hash: _Optional[str] = ..., peer_ip: _Optional[str] = ..., peer_asn: _Optional[int] = ..., timestamp: _Optional[str] = ..., igp_router_id: _Optional[str] = ..., protocol: _Optional[str] = ..., area_id: _Optional[str] = ..., nexthop: _Optional[str] = ..., local_node_hash: _Optional[str] = ..., mtid: _Optional[_Union[_base_pb2.MultiTopologyIdentifier, _Mapping]] = ..., prefix: _Optional[str] = ..., prefix_len: _Optional[int] = ..., prefix_metric: _Optional[int] = ..., is_prepolicy: bool = ..., is_adj_rib_in: bool = ...) -> None: ...

class LsSrv6Sid(_message.Message):
    __slots__ = ["domain_id", "id", "igp_flags", "igp_router_id", "is_adj_rib_in", "is_prepolicy", "key", "local_node_asn", "local_node_hash", "mtid", "nexthop", "peer_asn", "peer_hash", "peer_ip", "protocol", "router_hash", "router_ip", "srv6_sid", "timestamp"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IGP_FLAGS_FIELD_NUMBER: _ClassVar[int]
    IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADJ_RIB_IN_FIELD_NUMBER: _ClassVar[int]
    IS_PREPOLICY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NODE_ASN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NODE_HASH_FIELD_NUMBER: _ClassVar[int]
    MTID_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_HASH_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_HASH_FIELD_NUMBER: _ClassVar[int]
    ROUTER_IP_FIELD_NUMBER: _ClassVar[int]
    SRV6_SID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    id: str
    igp_flags: int
    igp_router_id: str
    is_adj_rib_in: bool
    is_prepolicy: bool
    key: str
    local_node_asn: int
    local_node_hash: str
    mtid: _base_pb2.MultiTopologyIdentifier
    nexthop: str
    peer_asn: int
    peer_hash: str
    peer_ip: str
    protocol: str
    router_hash: str
    router_ip: str
    srv6_sid: str
    timestamp: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., router_hash: _Optional[str] = ..., router_ip: _Optional[str] = ..., domain_id: _Optional[int] = ..., peer_hash: _Optional[str] = ..., peer_ip: _Optional[str] = ..., peer_asn: _Optional[int] = ..., timestamp: _Optional[str] = ..., igp_router_id: _Optional[str] = ..., local_node_asn: _Optional[int] = ..., protocol: _Optional[str] = ..., nexthop: _Optional[str] = ..., local_node_hash: _Optional[str] = ..., mtid: _Optional[_Union[_base_pb2.MultiTopologyIdentifier, _Mapping]] = ..., igp_flags: _Optional[int] = ..., is_prepolicy: bool = ..., is_adj_rib_in: bool = ..., srv6_sid: _Optional[str] = ...) -> None: ...

class Peer(_message.Message):
    __slots__ = ["id", "key", "local_bgp_id", "remote_bgp_id", "router_hash"]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_BGP_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BGP_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTER_HASH_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    local_bgp_id: str
    remote_bgp_id: str
    router_hash: str
    def __init__(self, key: _Optional[str] = ..., id: _Optional[str] = ..., router_hash: _Optional[str] = ..., remote_bgp_id: _Optional[str] = ..., local_bgp_id: _Optional[str] = ...) -> None: ...
