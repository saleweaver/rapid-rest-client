from setuptools import setup

from rest_client.__version__ import __version__

setup(
    name='rapid_rest_client',
    install_requires=[
        'requests',
        'colorlog'
    ],
    version=__version__,
    packages=['rest_client', 'rest_client.base'],
    url='',
    license='MIT',
    author='Michael Primke',
    author_email='michael@saleweaver.com',
    description='API Client'
)
