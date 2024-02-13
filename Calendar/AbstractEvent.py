from abc import ABC, abstractmethod
from icalendar import Event
class AbstractEvent(ABC):
    def __init__(self, given_event):
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
    def create_icalendar_event(self):
        pass