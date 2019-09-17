Install pyenv https://github.com/pyenv/pyenv

and then

pyenv-virtualenv https://github.com/pyenv/pyenv-virtualenv

run:

`pip install grpcio-tools`

Then generate the bindings:
$ `python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/catan.proto`

Finally, run the client (and make sure you have the scala server running locally)
`python client.py`

For python grpc reference: https://grpc.io/docs/tutorials/basic/python/
