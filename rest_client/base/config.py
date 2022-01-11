import json
import pprint
import re
from dataclasses import dataclass, field

import requests
from requests.structures import CaseInsensitiveDict

from .exceptions import ConfigurationException


def make_query(p):
    r = r'{.*}'
    try:
        return re.sub(r, '{}', p), p[p.index('{') + 1:p.index('}')], True
    except ValueError:
        return re.sub(r, '{}', p), None, False


def sub(e):
    return re.sub(r'([A-Z])', lambda match: r'_{}'.format(match.group(1).lower()), e[0].lower() + e[1:])


@dataclass(frozen=True)
class BaseUrlConfig:
    base_url: str
    sandbox_url: str or None = None
    options: dict = field(default=dict)


@dataclass
class RequestConfig:
    path: str
    name: str
    method: str = 'GET'
    options: dict = field(default=dict)


class ApiResponse:
    def __init__(self, data=None, headers: CaseInsensitiveDict = None, status_code: int = None, **kwargs):
        self.status_code: int = status_code
        self.payload = data or kwargs
        self.headers: CaseInsensitiveDict = headers

    def __str__(self):
        return pprint.pformat(vars(self))


class ApiConfiguration(object):
    def __init__(self, endpoints: [RequestConfig], base_url_config: BaseUrlConfig):
        self._endpoints = endpoints
        self._base_url_config = base_url_config

    def __call__(self, cls):
        n = {}
        for _endpoint in self._endpoints:
            n.update({
                _endpoint.name: _endpoint
            })
        cls.endpoints = n
        cls.base_url_config = self._base_url_config
        cls.__dir__ = self._dir(cls, cls.endpoints.keys())
        return cls

    @staticmethod
    def _dir(cls, endpoint_keys):
        def _dir(_cls):
            res = dir(type(cls)) + list(cls.__dict__.keys())
            res.extend(endpoint_keys)
            return res
        return _dir(cls)


class DictApiConfiguration(ApiConfiguration):
    def __init__(self, endpoints: list, base_url_config: BaseUrlConfig):
        _endpoints = [RequestConfig(
            path=e['path'],
            name=e['name'],
            method=e.get('method', 'GET'),
            options=e.get('options', {})
        ) for e in endpoints]
        super(DictApiConfiguration, self).__init__(_endpoints, base_url_config)


class JsonApiConfiguration(DictApiConfiguration):
    def __init__(self, endpoints: str, base_url_config: BaseUrlConfig):
        super(JsonApiConfiguration, self).__init__(json.loads(endpoints), base_url_config)


class SwaggerApiConfiguration(ApiConfiguration):
    def __init__(self,
                 base_url_config: BaseUrlConfig,
                 url: str = None,
                 definition: dict = None):
        if url is None and definition is None:
            raise ConfigurationException('url or definition must be set')
        if url is not None:
            definition = requests.get(url).json()

        operations = []
        for k, v in definition.get('paths').items():
            for method, val in v.items():
                if method == 'parameters':
                    continue
                uri, param, has_query_params = make_query(k)
                operation = {
                    'uri': uri,
                    'method': method.upper(),
                    'has_query_params': has_query_params,
                    'query_param': param,
                    'params_or_data': 'params' if method == 'get' else 'data',
                    'title': sub(val.get('operationId')),
                    'description': val.get('description')
                }
                operations.append(operation)

        endpoints = [RequestConfig(
            path=e['uri'],
            name=e['title'],
            method=e.get('method', 'GET'),
            options=e.get('options', {})
        ) for e in operations]
        super().__init__(endpoints, base_url_config)
