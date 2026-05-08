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

### Create user room

```python
client.rooms.create_from_user(room_args)
```

### List user room

```python
client.rooms.list_from_user()
```

### Create user room message

```python
client.rooms.create_message_from_user()
```

### List user room messages

```python
client.rooms.list_messages_from_user()
```

### Search user messages

```python
client.rooms.search_messages_from_user(search='found')
```

### List all identities in the tenant

```python
client.identities.list(tenant_uuid=<tenant_uuid>)
```

### Get an identity by UUID

```python
client.identities.get(<identity_uuid>, tenant_uuid=<tenant_uuid>)
```

### Create an identity

```python
client.identities.create(
    {
        'user_uuid': <user_uuid>,
        'backend': <backend>,
        'type': <type>,
        'identity': <identity>,
    },
    tenant_uuid=<tenant_uuid>,
)
```

### Update an identity

```python
client.identities.update(
    <identity_uuid>,
    {'identity': <new_identity>},  # or {'user_uuid': <new_user_uuid>} to reassign
    tenant_uuid=<tenant_uuid>,
)
```

### Delete an identity

```python
client.identities.delete(<identity_uuid>, tenant_uuid=<tenant_uuid>)
```

### List the authenticated user's own identities

```python
client.identities.list_from_user()
```
