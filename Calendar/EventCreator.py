from abc import ABC, abstractmethod
from icalendar import Event


class EventCreator(ABC):
    def __init__(self, given_event):
        '''
        Base class for iCalendar event formatting.
        :param given_event: Event to create an iCalendar event for.
        '''
        self._given_event = given_event
        self._week_days_mapping = {
            'Luni': 'MO',
            'Marti': 'TU',
            'Miercuri': 'WE',
            'Joi': 'TH',
            'Vineri': 'FR',
            'Sambata': 'SA',
            'Duminica': 'SU'
        }

    @abstractmethod
    def create_icalendar_event(self) -> Event:
        '''
        Transforms the given event into an iCalendar event.
        '''
        pass
