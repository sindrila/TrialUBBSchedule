from Calendar.ProfessorCalendarCreator import ProfessorCalendarCreator
from Repository.Repository import Repository
from Service.CalendarService import CalendarService


class ProfessorScheduleCalendarService(CalendarService):
    def __init__(self, repository: Repository):
        '''
        Service for creating calendar schedules for professors.
        :param repository: Repository with data about professor and classes.
        '''
        super().__init__(repository)

    def generate_calendars(self) -> None:
        '''
        Generates calendar schedules for professors and writes them into files.
        '''
        professors_and_classes = self._repository.get_data()
        index = 0
        for professors_and_class in professors_and_classes:
            index += 1
            professor = professors_and_class[0]
            classes = professors_and_class[1][1:]
            professor_scheduler_ical = ProfessorCalendarCreator(classes)
            professor_calendar = professor_scheduler_ical.generate_icalendar_for_schedule()
            file_name = professor.name.replace(' ', '_')
            with open(f'ProfessorCalendars/{file_name}.ics', 'wb') as file:
                file.write(professor_calendar)
