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

### Get the current status of wazo-chatd

```python
client.status.get()
```

### List all user presences

```python
client.user_presences.list()
```

### Get a user presence

```python
client.user_presences.get(<user_uuid>)
```

### Update a user presence

```python
client.user_presences.update(user_args)
```
