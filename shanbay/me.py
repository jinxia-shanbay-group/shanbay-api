from .common import *
from .people import People
class Me(People):
    def __init__(self):
        super().__init__()

    def send_msg(self, people, content):
        ...
