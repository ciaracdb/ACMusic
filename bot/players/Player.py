import random
from abc import ABCMeta, abstractmethod
from queue import Queue

class Player(metaclass=ABCMeta):
    def __init__(self, client):
        self.client = client
        self.queue = Queue()

    def addToQueue(self, url):
        self.queue.put(url)

    @abstractmethod
    async def startQueue(self):
        return NotImplemented

    @abstractmethod
    async def next(self):
        return NotImplemented

    @abstractmethod
    def pause(self):
        return NotImplemented

    @abstractmethod
    def resume(self):
        return NotImplemented

    @abstractmethod
    def stop(self):
        return NotImplemented

    def shuffle(self):
        x = list()
        while not self.queue.empty():
            x.append(self.queue.get())
        random.shuffle(x)
        for i in x:
            self.addToQueue(i)