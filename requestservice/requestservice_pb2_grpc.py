# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from requestservice import requestservice_pb2 as requestservice_dot_requestservice__pb2


class RequestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLsNodes = channel.unary_unary(
                '/jagw.RequestService/GetLsNodes',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsNodeResponse.FromString,
                )
        self.GetLsLinks = channel.unary_unary(
                '/jagw.RequestService/GetLsLinks',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsLinkResponse.FromString,
                )
        self.GetLsPrefixes = channel.unary_unary(
                '/jagw.RequestService/GetLsPrefixes',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsPrefixResponse.FromString,
                )
        self.GetLsSrv6Sids = channel.unary_unary(
                '/jagw.RequestService/GetLsSrv6Sids',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsSrv6SidResponse.FromString,
                )
        self.GetLsNodeEdges = channel.unary_unary(
                '/jagw.RequestService/GetLsNodeEdges',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsNodeEdgeResponse.FromString,
                )
        self.GetPeers = channel.unary_unary(
                '/jagw.RequestService/GetPeers',
                request_serializer=requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.PeerResponse.FromString,
                )
        self.GetLsNodeCoordinates = channel.unary_unary(
                '/jagw.RequestService/GetLsNodeCoordinates',
                request_serializer=requestservice_dot_requestservice__pb2.LsNodeCoordinatesRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.LsNodeCoordinatesResponse.FromString,
                )
        self.GetTelemetryData = channel.unary_unary(
                '/jagw.RequestService/GetTelemetryData',
                request_serializer=requestservice_dot_requestservice__pb2.TelemetryRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.TelemetryResponse.FromString,
                )
        self.GetMeasurements = channel.unary_unary(
                '/jagw.RequestService/GetMeasurements',
                request_serializer=requestservice_dot_requestservice__pb2.MeasurementsRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.MeasurementsResponse.FromString,
                )
        self.GetMeasurementDetails = channel.unary_unary(
                '/jagw.RequestService/GetMeasurementDetails',
                request_serializer=requestservice_dot_requestservice__pb2.MeasurementDetailsRequest.SerializeToString,
                response_deserializer=requestservice_dot_requestservice__pb2.MeasurementDetailsResponse.FromString,
                )


class RequestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLsNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLsLinks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLsPrefixes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLsSrv6Sids(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLsNodeEdges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLsNodeCoordinates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTelemetryData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMeasurements(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMeasurementDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLsNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsNodes,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsNodeResponse.SerializeToString,
            ),
            'GetLsLinks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsLinks,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsLinkResponse.SerializeToString,
            ),
            'GetLsPrefixes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsPrefixes,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsPrefixResponse.SerializeToString,
            ),
            'GetLsSrv6Sids': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsSrv6Sids,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsSrv6SidResponse.SerializeToString,
            ),
            'GetLsNodeEdges': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsNodeEdges,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsNodeEdgeResponse.SerializeToString,
            ),
            'GetPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeers,
                    request_deserializer=requestservice_dot_requestservice__pb2.TopologyRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.PeerResponse.SerializeToString,
            ),
            'GetLsNodeCoordinates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLsNodeCoordinates,
                    request_deserializer=requestservice_dot_requestservice__pb2.LsNodeCoordinatesRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.LsNodeCoordinatesResponse.SerializeToString,
            ),
            'GetTelemetryData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetryData,
                    request_deserializer=requestservice_dot_requestservice__pb2.TelemetryRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.TelemetryResponse.SerializeToString,
            ),
            'GetMeasurements': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasurements,
                    request_deserializer=requestservice_dot_requestservice__pb2.MeasurementsRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.MeasurementsResponse.SerializeToString,
            ),
            'GetMeasurementDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasurementDetails,
                    request_deserializer=requestservice_dot_requestservice__pb2.MeasurementDetailsRequest.FromString,
                    response_serializer=requestservice_dot_requestservice__pb2.MeasurementDetailsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jagw.RequestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RequestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLsNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsNodes',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLsLinks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsLinks',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLsPrefixes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsPrefixes',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsPrefixResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLsSrv6Sids(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsSrv6Sids',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsSrv6SidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLsNodeEdges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsNodeEdges',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsNodeEdgeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetPeers',
            requestservice_dot_requestservice__pb2.TopologyRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.PeerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLsNodeCoordinates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetLsNodeCoordinates',
            requestservice_dot_requestservice__pb2.LsNodeCoordinatesRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.LsNodeCoordinatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTelemetryData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetTelemetryData',
            requestservice_dot_requestservice__pb2.TelemetryRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.TelemetryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMeasurements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetMeasurements',
            requestservice_dot_requestservice__pb2.MeasurementsRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.MeasurementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMeasurementDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jagw.RequestService/GetMeasurementDetails',
            requestservice_dot_requestservice__pb2.MeasurementDetailsRequest.SerializeToString,
            requestservice_dot_requestservice__pb2.MeasurementDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
