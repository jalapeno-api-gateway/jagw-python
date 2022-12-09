from jagw.channel import create_channel
from requestservice.requestservice_pb2_grpc import RequestServiceStub
from requestservice.requestservice_pb2 import TopologyRequest

HOST = '172.16.19.66'
PORT = '9903'

def get_all_lsnodes():
    channel = create_channel(HOST, PORT)
    with channel:
        stub = RequestServiceStub(channel)
        response = stub.GetLsNodes(TopologyRequest())
        print(response)

get_all_lsnodes()


