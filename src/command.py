
from observable import Observable

class Command(Observable):

    def __init__(self):
        Observable.__init__(self)

    def execute(self, screen):
        raise NotImplementedError