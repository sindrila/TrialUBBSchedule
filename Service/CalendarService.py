from abc import ABC, abstractmethod

from Repository.Repository import Repository


class CalendarService(ABC):
    def __init__(self, repository: Repository):
        '''
        Base class for a service
        :param repository: Repository with data.
        '''
        self._repository = repository

    @abstractmethod
    def generate_calendars(self):
        '''
        Abstract method that generates calendars for the data in repository.
        '''
        pass
