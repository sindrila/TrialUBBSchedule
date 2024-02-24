from Domain.Class import Class
from Domain.ClassType import ClassType
from Domain.Frequency import Frequency
from Domain.Professor import Professor
from Domain.Room import Room
from Domain.Subject import Subject


class StudentClass(Class):
    def __init__(self, day: str, starting_hour: int, ending_hour: int, frequency: Frequency, room: Room, formation: str,
                 class_type: ClassType, subject: Subject, professor: Professor):
        '''
        Represents a class for a group of students.
        :param day: String representing the day of the week.
        :param starting_hour: Integer representing the starting hour.
        :param ending_hour: Integer representing the ending hour.
        :param frequency: Frequency representing the weekly/first week/second week.
        :param room: Room representing the room in which the class is located.
        :param formation: String representing the formation.
        :param class_type: ClassType representing the class type.
        :param subject: Subject representing the name of the class.
        :param professor: Professor of the class.
        '''
        super().__init__(day, int(starting_hour), int(ending_hour), frequency, room, formation, class_type, subject)
        self._professor = professor

    @property
    def professor(self):
        return self._professor

    def __str__(self):
        output = "Student Class" + "\n"
        output += "Day: " + self._day + "\n"
        output += "Hours: " + str(self._starting_hour) + "-" + str(self._ending_hour) + "\n"
        output += "Frequency: " + str(self._frequency.value) + "\n"
        output += "Room: " + str(self._room) + "\n"
        output += "Formation: " + self._formation + "\n"
        output += "Class type: " + str(self._class_type.value) + "\n"
        output += "Subject: " + str(self._subject) + "\n"
        output += "Professor: " + str(self._professor) + "\n"
        return output
