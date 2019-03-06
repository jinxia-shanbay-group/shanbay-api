import requests
from .common import *


class ShanbayClient:
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(DefaultHeader)

    def login(self):
        ...

    def login_with_cookies(self):
        ...

    def login_in_terminal(self):
        ...

    def create_cookies(self):
        ...

    def set_proxy(self):
        ...

    def set_proxy_tool(self):
        ...

    def remove_proxy_pool(self):
        ...

    def me(self):
        ...

    def __getattr__(self, item):
        ...
