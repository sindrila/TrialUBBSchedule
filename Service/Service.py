from abc import ABC, abstractmethod

from Repository.Repository import Repository


class Service(ABC):
    def __init__(self, repository: Repository):
        self._repository = repository

    @abstractmethod
    def generate_calendars(self):
        pass
