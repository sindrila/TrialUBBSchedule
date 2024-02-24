from Calendar.StudentCalendarCreator import StudentCalendarCreator
from Repository.Repository import Repository
from Service.CalendarService import CalendarService


class StudentScheduleCalendarService(CalendarService):
    def __init__(self, repository: Repository):
        '''
        Service for creating calendar schedules for students.
        :param repository: Repository with data about year of study and classes
        '''
        super().__init__(repository)
        self._repository = repository

    def generate_calendars(self):
        '''
        Generates calendar schedules for students and writes them to files.
        '''
        student_years_and_classes = self._repository.get_data()
        index = 0
        for student_year_and_class in student_years_and_classes:
            index += 1
            year = student_year_and_class[0]
            if student_year_and_class[1]:
                for group in student_year_and_class[1].keys():
                    print(f"Year {year} group {group}")
                    # for class_name in student_year_and_class[1][group]:
                    #     print(class_name)
                    student_schedule_ical = StudentCalendarCreator(student_year_and_class[1][group])
                    year_calendar = student_schedule_ical.generate_icalendar_for_schedule()
                    file_name = f"{group}.ics"
                    file_name = file_name.replace("/", "-")
                    print(file_name)
                    with open(f'StudentCalendars/{file_name}', 'wb') as file:
                        file.write(year_calendar)