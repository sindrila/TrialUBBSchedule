from abc import ABC, abstractmethod

from Domain.Class import Class


class AbstractClassScheduler(ABC):
    def __init__(self, data: list[Class]):
        self._data = data
    @abstractmethod
    def generate_icalendar_for_schedule(self):
        pass
