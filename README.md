# wazo-chatd-client

A python client library to access wazo-chatd

## Usage

### Creating a client

```python
from wazo_chatd_client import Client
client = Client('localhost', verify_certificate=False, token=<auth-token>)
```

## Config

### Getting the service configuration

```python
client.config.get()
```
