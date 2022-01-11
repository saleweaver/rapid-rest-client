REST-CLIENT
===========

Setup a client in minutes

```python
from rest_client.base import BaseUrlConfig, ApiConfiguration, RequestConfig, Client

endpoint_config: BaseUrlConfig = BaseUrlConfig('https://reqres.in/api/')

@ApiConfiguration(endpoints=[
    RequestConfig('users', 'list_users'),
    RequestConfig('users/{}', 'get_user'),
    RequestConfig('register', 'register_user', 'POST')
], base_url_config=endpoint_config)
class ExampleClient(Client):
    pass

```

This makes available these methods on `ExampleClient`

- list_users
- get_user 
- register_user

```python
client = ExampleClient()
list_users_response = client.list_users()
get_user_response = client.get_user(3)
register_user_response = client.register_user(email="eve.holt@reqres.in", password="pistol")
```

You can also create the client from json, or a dict:

````python
from rest_client.base import DictApiConfiguration, BaseUrlConfig, Client

endpoint_config: BaseUrlConfig = BaseUrlConfig('https://reqres.in/api/')

@DictApiConfiguration(endpoints=[{
    'path': 'users',
    'name': 'list_users',
}], base_url_config=endpoint_config)
class MyClient(Client):
    pass
````

### Authentication

You can pass custom authentication through the `authentication_handler` property. Authentication handlers should extend AuthBase from `requests.auth`

For example: 

```python
from rest_client.base import BaseUrlConfig, ApiConfiguration, RequestConfig, Client, BearerTokenAuth

auth_endpoint_config: BaseUrlConfig = BaseUrlConfig('https://gorest.co.in/public/v1/')

@ApiConfiguration(
    endpoints=[
        RequestConfig('users', 'register_user', 'POST'),
    ],
    base_url_config=auth_endpoint_config)
class AuthClient(Client):
    pass

auth_client = AuthClient(
    authentication_handler=BearerTokenAuth('token')
)
```

---

Please note:

This is a work in progress and completely new. Contributions are very welcome. 

