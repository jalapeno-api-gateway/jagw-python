<p align="center">
	<img src="./docs/jagw-logo.png">
</p>
<h1 align="center">JAGW-Python</h1>
<p align="center">
	<a href="https://github.com/jalapeno-api-gateway/jagw-python/releases/latest"><img src="https://img.shields.io/github/v/tag/jalapeno-api-gateway/jagw-python.svg?label=release&logo=github&style=flat-square" alt="Latest"></a>
</p>

<p align="center">
The JAGW-Python repository contains a Python client library for interacting with the Jalapeno API Gateway
</p>

---

## Documentation
Documentation can be found under https://jalapeno-api-gateway.github.io/jagw.

## Example
Here is a list of code examples with short description of demonstrated JAGW-Go functionality:

- [request-all-nodes](examples/request_all_nodes.py) - request all lsnodes from the gateway

All code examples can be found under [examples](examples) directory.

## Quick Start
Below are short code samples showing a JAGW-Python client interacting with the Jalapeno API Gateway.

```python
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
```
Complete example in [request_all_nodes.py](examples/request_all_nodes.py)

## How to contribute?

- Contribute code by submitting a [Pull Request](https://github.com/jalapeno-api-gateway/jagw-python/pulls).
- Report bugs by opening an [Issue](https://github.com/jalapeno-api-gateway/jagw-python/issues).
- Ask questions & open discussions by starting a [Discussion](https://github.com/jalapeno-api-gateway/jagw-python/discussions).