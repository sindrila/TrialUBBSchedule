from abc import ABC, abstractmethod

class Repository(ABC):
    def __init__(self):
        self._data = None
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def serialize_data(self):
        pass
