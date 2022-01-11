from dataclasses import FrozenInstanceError

import pytest

from rest_client.base.config import BaseUrlConfig
base_url = 'https://www.saleweaver.com/'


def test_create_endpoint_config():
    endpoint_config = BaseUrlConfig(base_url)
    assert endpoint_config.base_url == base_url
    assert endpoint_config.sandbox_url is None


def test_fail_on_assign():
    endpoint_config = BaseUrlConfig(base_url)
    with pytest.raises(FrozenInstanceError) as excinfo:
        endpoint_config.sandbox_url = 'Foo'
    assert excinfo.type == FrozenInstanceError

