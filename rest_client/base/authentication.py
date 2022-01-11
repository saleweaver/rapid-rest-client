from requests.auth import AuthBase


class Authentication(AuthBase):
    pass


class BearerTokenAuth(Authentication):
    def __init__(self, token, _type='Bearer'):
        self.token = token
        self.type = _type

    def __call__(self, r):
        r.headers['Authorization'] = f'{self.type} {self.token}'
        return r

