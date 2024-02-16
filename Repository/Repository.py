from abc import ABC, abstractmethod

class Repository(ABC):
    def __init__(self):
        '''
        Base class for a repository.
        '''
        self._data = None
    @abstractmethod
    def get_data(self):
        '''
        Get data from the repository.
        '''
        pass

    @abstractmethod
    def serialize_data(self) -> None:
        '''
        Serialize data into a pickle binary dump.
        '''
        pass
