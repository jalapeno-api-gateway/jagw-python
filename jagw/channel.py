import grpc
from grpc import experimental, Channel

def create_channel(endpoint_address: str, endpoint_port: int) -> Channel:
    """
    Creates a new GRPC channel.

    Args:
        endpoint_address: Address of the JAGW Endpoint
        endpoint_port: Port of the JAGW Endpoint
    Returns:
        A GRPC channel
    """
    channel_options = [(experimental.ChannelOptions.SingleThreadedUnaryStream, 1)]
    return grpc.insecure_channel(f"{endpoint_address}:{endpoint_port}", options=channel_options)
