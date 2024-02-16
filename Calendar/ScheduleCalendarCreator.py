from abc import ABC, abstractmethod
from icalendar import Calendar
from Domain.Class import Class


class ScheduleCalendarCreator(ABC):
    def __init__(self, data: list[Class]):
        '''
        Base class for iCalendar calendar formatting.
        :param data: List of Classes for scheduling
        '''
        self._data = data

    @abstractmethod
    def generate_icalendar_for_schedule(self) -> Calendar:
        '''
        Transforms a list of classes into an iCalendar calendar.
        '''
        pass
