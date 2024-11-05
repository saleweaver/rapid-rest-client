from rest_client.base.config import RequestConfig


def fill_query_params(query, *args):
    return query.format(*args)


def endpoint(path: str, name: str = None, method: str = 'GET', options: dict = None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            kwargs.update({
                'request_config': RequestConfig(
                    path=fill_query_params(path, *args),
                    name=name or path,
                    method=method,
                    options=options)
            })
            return function(*args, **kwargs)

        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator

