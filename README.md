REST-CLIENT
===========

![Tests](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRy81RXhCL21iaEJXaHRieUg3Ly9IOVNkZjIvNWI4MmdGNG5sb2phR1pWNUk1TS9Xb0V6c2srL2hOMitobjNYOURueXR0eXVqTmV2M09XbWg1TFhwTW13PSIsIml2UGFyYW1ldGVyU3BlYyI6Ijk4V2xzeWp2K29uU0RNNDMiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

Setup a client in minutes

---

### Installation

````bash
pip install rapid-rest-client
````

### Usage

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

This makes these methods available on `ExampleClient`

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

---

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=saleweaver_rapid_rest_client)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=coverage)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=bugs)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_rapid_rest_client&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=saleweaver_rapid_rest_client)
