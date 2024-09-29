from abc import ABC


from Domain.ClassType import ClassType
from Domain.Frequency import Frequency
from Domain.Room import Room
from Domain.Subject import Subject


class Class(ABC):
    def __init__(self, day: str, starting_hour: int, ending_hour: int, frequency: Frequency, room: Room,
                 formation: str, class_type: ClassType, subject: Subject):
        '''
        Represents a class in the schedule.
        :param day: String representing the day of the week.
        :param starting_hour: Integer representing the starting hour of the class.
        :param ending_hour: Integer representing the ending hour of the class.
        :param frequency: Frequency representing the weekly/first week/second week
        :param room: Room representing the room in which the class is located.
        :param formation: String representing the formation.
        :param class_type: ClassType representing the class type.
        :param subject: Subject representing the name of the class.
        '''
        self._day: str = day
        self._starting_hour: int = int(starting_hour)
        self._ending_hour: int = int(ending_hour)
        self._frequency: Frequency = frequency
        self._room: Room = room
        self._formation: str = formation
        self._class_type: ClassType = class_type
        self._subject: Subject = subject

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
        self._starting_hour = int(value)

    @property
    def ending_hour(self) -> int:
        return self._ending_hour

    @ending_hour.setter
    def ending_hour(self, value: int):
        self._ending_hour = int(value)

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

    @property
    def subject(self):
        return self._subject

    def is_same_class_different_formation(self, other):
        '''
        Two classes are considered the same if they are at the same time, with the same week frequency.
        This checks if multiple formations attend a class.
        :param other: Class to compare.
        '''
        return (self._day == other.day and
                self._starting_hour == other.starting_hour and
                self._ending_hour == other.ending_hour and
                self._frequency == other.frequency and
                self._formation != other.formation)
