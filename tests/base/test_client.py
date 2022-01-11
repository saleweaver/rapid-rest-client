from rest_client.base import BearerTokenAuth
from rest_client.base import Client
from rest_client.base import BaseUrlConfig, RequestConfig, ApiConfiguration, DictApiConfiguration
from rest_client.base import ApiException

endpoint_config: BaseUrlConfig = BaseUrlConfig('https://reqres.in/api/', 'https://sandbox.reqres.in/api/')
auth_endpoint_config: BaseUrlConfig = BaseUrlConfig('https://gorest.co.in/public/v1/')


@ApiConfiguration(endpoints=[
    RequestConfig('users', 'list_users'),
    RequestConfig('users/{}', 'get_user'),
    RequestConfig('register', 'register_user', 'POST')
], base_url_config=endpoint_config)
class ExampleClient(Client):
    pass


no_auth_client = ExampleClient()


@ApiConfiguration(
    endpoints=[
        RequestConfig('users', 'register_user', 'POST'),
    ],
    base_url_config=auth_endpoint_config)
class AuthClient(Client):
    pass


auth_client = AuthClient(
    authentication_handler=BearerTokenAuth('c0bc41334b0196da778878e94ad3531f98fee634839564eef174529994bf6263')
)


# JsonConfigurationClient
@DictApiConfiguration(endpoints=[{
    'path': 'users',
    'name': 'list_users_json_endpoint',
}], base_url_config=endpoint_config)
class JsonConfiguredClient(Client):
    pass


json_configured_client = JsonConfiguredClient()


def test_request_no_auth():
    res = no_auth_client.list_users()
    assert res.payload.get('page') == 1


def test_request_no_auth_with_query_params():
    res = no_auth_client.get_user(2)
    assert res.payload.get('data').get('id') == 2


def test_register_user_post():
    res = no_auth_client.register_user(email="eve.holt@reqres.in", password="pistol")
    assert res.payload.get('id') == 4


def test_register_user_post_with_bearer_auth():
    try:
        res = auth_client.register_user(
            **{"name": "Tenali Ramakrishna", "gender": "male", "email": "fhtderze@15ce.com", "status": "active"})
        assert res.status_code == 201
    except ApiException as e:
        assert e.status_code == 422


def test_json_configured_client():
    res = json_configured_client.list_users_json_endpoint()
    assert res.status_code == 200
