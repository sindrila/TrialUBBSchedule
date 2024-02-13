import os
import subprocess

from Calendar.AbstractClassScheduler import AbstractClassScheduler
from Calendar.ProfessorEvent import ProfessorEvent
from Domain.ClassProfessor import ClassProfessor
from icalendar import Calendar


class ProfessorScheduler(AbstractClassScheduler):
    def __init__(self, professor_data: list[ClassProfessor]):
        '''
        self._data: list[ClassProfessor]
        '''
        super().__init__(professor_data)

    def sanitize_overlapping_classes(self):
        for individual_class1 in self._data:
            for individual_class2 in self._data:
                if individual_class1.is_same_class_different_formation(individual_class2):
                    individual_class1.formation += f", {individual_class2.formation}"
                    self._data.remove(individual_class2)

    def generate_icalendar_for_schedule(self):
        cal = Calendar()
        cal.add('prodid', '-//Facultatea de Matematica si Informatica//Orar//RO')
        cal.add('X-WR-CALNAME', 'Orar UBB Matematica si Informatica')

        self.sanitize_overlapping_classes()

        for individual_class in self._data:
            event = ProfessorEvent(individual_class)
            cal.add_component(event.create_icalendar_event())

        return cal.to_ical()
