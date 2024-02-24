from Calendar.ScheduleCalendarCreator import ScheduleCalendarCreator
from Calendar.StudentEventCreator import StudentEventCreator
from Domain.StudentClass import StudentClass
from icalendar import Calendar


class StudentCalendarCreator(ScheduleCalendarCreator):
    def __init__(self, student_data: list[StudentClass]):
        super().__init__(student_data)

    def generate_icalendar_for_schedule(self) -> Calendar:
        '''
        :return: iCalendar calendar containing a professor's classes.
        '''
        cal = Calendar()
        cal.add('prodid', '-//Facultatea de Matematica si Informatica//Orar//RO')
        cal.add('X-WR-CALNAME', 'Orar UBB Matematica si Informatica')

        for individual_class in self._data:
            event = StudentEventCreator(individual_class)
            cal.add_component(event.create_icalendar_event())

        return cal.to_ical()