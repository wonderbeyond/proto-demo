# Demo project to reproduce betterproto's SerializeToString issue

**The problem itself:**

Using betterproto, when a timestamp field value is explicitly `1970-01-01T00:00:00+00:00`,
then the serialized bytes would be the same as if it's not set (or set None).

However while using the official compiler,
we can distinguish the explicitly set zero values and the unset values.

---

## Prepare the Python environment

```
pyenv virtualenv 3.10.1 proto-demo
pyenv local proto-demo
pip install -r requirements.txt
```


## Compile proto with official tool
```
python -m grpc_tools.protoc -I protos \
    --python_out=. --grpc_python_out=. \
    protos/demo.proto
```

## Compile proto with betterproto

```
python -m grpc_tools.protoc -I protos \
    --python_betterproto_out=better_pb2 \
    protos/demo.proto
```

## Reveal the issue

```
python reveal.py
```
