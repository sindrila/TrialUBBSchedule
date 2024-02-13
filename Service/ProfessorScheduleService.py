from Calendar.ProfessorScheduler import ProfessorScheduler
from Domain.Professor import Professor
from Parsers.ProfessorPageParser import ProfessorPageParser
from PickleSerializer import PickleSerializer
from Repository.Repository import Repository
from Service.Service import Service


class ProfessorScheduleService(Service):
    def __init__(self, repository: Repository):
        super().__init__(repository)

    def generate_calendars(self):
        print("Generating calendars...")
        professors_and_classes = self._repository.get_data()
        index = 0
        for professors_and_class in professors_and_classes:
            index += 1
            professor = professors_and_class[0]
            classes = professors_and_class[1][1:]
            professor_scheduler_ical = ProfessorScheduler(classes)
            professor_calendar = professor_scheduler_ical.generate_icalendar_for_schedule()
            file_name = professor.name.replace(' ', '_')
            with open(f'ProfessorCalendars/{file_name}.ics', 'wb') as file:
                file.write(professor_calendar)

