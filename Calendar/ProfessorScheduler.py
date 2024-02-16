from Calendar.ScheduleCalendarCreator import ScheduleCalendarCreator
from Calendar.ProfessorEvent import ProfessorEventCreator
from Domain.ProfessorClass import ProfessorClass
from icalendar import Calendar


class ProfessorCalendarCreator(ScheduleCalendarCreator):
    def __init__(self, professor_data: list[ProfessorClass]):
        '''
        Calendar creator for professor classes.
        :param professor_data: List of all classes for a professor.
        '''
        super().__init__(professor_data)

    def sanitize_overlapping_classes(self):
        '''
        Helper method to sanitize overlapping professor classes (same class, more student groups attending).
        Reduces all overlapping classes into a single class with formations appended.
        '''
        for individual_class1 in self._data:
            for individual_class2 in self._data:
                if individual_class1.is_same_class_different_formation(individual_class2):
                    individual_class1.formation += f", {individual_class2.formation}"
                    self._data.remove(individual_class2)

    def generate_icalendar_for_schedule(self) -> Calendar:
        '''
        :return: iCalendar calendar containing a professor's classes.
        '''
        cal = Calendar()
        cal.add('prodid', '-//Facultatea de Matematica si Informatica//Orar//RO')
        cal.add('X-WR-CALNAME', 'Orar UBB Matematica si Informatica')

        self.sanitize_overlapping_classes()

        for individual_class in self._data:
            event = ProfessorEventCreator(individual_class)
            cal.add_component(event.create_icalendar_event())

        return cal.to_ical()
