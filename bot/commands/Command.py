from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def __init__(self, client):
        self.client = client

    @abstractmethod
    async def execute(self, message):
        return NotImplemented
