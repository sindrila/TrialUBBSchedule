from abc import ABC

from Domain.ClassType import ClassType
from Domain.Frequency import Frequency
from Domain.Frequency import get_frequency_from_string
from Domain.Room import Room


class Class(ABC):
    def __init__(self, day: str, starting_hour: int, ending_hour: int, frequency: Frequency, room: Room,
                 year_of_study: str, formation: str, class_type: ClassType):
        self._day: str = day
        self._starting_hour: int = starting_hour
        self._ending_hour: int = ending_hour
        self._frequency: Frequency = get_frequency_from_string(frequency)
        self._room: Room = room
        self._year_of_study: str = year_of_study
        self._formation: str = formation
        self._class_type: ClassType = class_type

    @property
    def day(self) -> str:
        return self._day

    @day.setter
    def day(self, value: str):
        self._day = value

    @property
    def starting_hour(self) -> int:
        return self._starting_hour

    @starting_hour.setter
    def starting_hour(self, value: int):
        self._starting_hour = value

    @property
    def ending_hour(self) -> int:
        return self._ending_hour

    @ending_hour.setter
    def ending_hour(self, value: int):
        self._ending_hour = value

    @property
    def frequency(self) -> Frequency:
        return self._frequency

    @frequency.setter
    def frequency(self, value: Frequency):
        self._frequency = value

    @property
    def room(self) -> Room:
        return self._room

    @room.setter
    def room(self, value: Room):
        self._room = value

    @property
    def year_of_study(self) -> str:
        return self._year_of_study

    @year_of_study.setter
    def year_of_study(self, value: str):
        self._year_of_study = value

    @property
    def formation(self) -> str:
        return self._formation

    @formation.setter
    def formation(self, value: str):
        self._formation = value

    @property
    def class_type(self) -> ClassType:
        return self._class_type

    @class_type.setter
    def class_type(self, value: ClassType):
        self._class_type = value
