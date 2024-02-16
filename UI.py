from Repository.ProfessorScheduleParserRepository import ProfessorScheduleParserRepository
from Repository.ProfessorSchedulePickleDumpRepository import ProfessorSchedulePickleDumpRepository
from Repository.Repository import Repository
from Service.ProfessorScheduleCalendarService import ProfessorScheduleCalendarService
from Service.CalendarService import CalendarService


class UI:
    def __init__(self):
        self._repository: Repository = None
        self._service: CalendarService = None

    def start(self):
        choice = -1
        while choice != 0:
            print("1. Create professor schedule using parser.")
            print("2. Create professor schedule using serialized data.")
            print("0. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self._repository = ProfessorScheduleParserRepository()
                self._service = ProfessorScheduleCalendarService(self._repository)
                print("Generating calendars...")
                self._service.generate_calendars()
                print("Calendars saved in ProfessorCalendars/")
                choice = 0
            elif choice == 2:
                self._repository = ProfessorSchedulePickleDumpRepository()
                self._service = ProfessorScheduleCalendarService(self._repository)
                print("Generating calendars...")
                self._service.generate_calendars()
                print("Calendars saved in ProfessorCalendars/")
                choice = 0
            elif choice != 0:
                print("Invalid choice. Please try again.")
        print("Goodbye.")
