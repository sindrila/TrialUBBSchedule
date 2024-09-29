from Parsers.StudentYearPageParser import StudentYearPageParser
from Repository.PickleSerializer import PickleSerializer
from Repository.Repository import Repository
from pathlib import Path

class StudentScheduleParserRepository(Repository):
    def __init__(self, student_page: str = 'https://www.cs.ubbcluj.ro/files/orar/2023-2/tabelar/index.html'):
        '''
        Repository for student schedule parser. Populates data by parsing.
        :param student_page: URL of student schedules page
        '''
        super().__init__()
        self._student_page = student_page
        self._data = self._parse_student_page()
        self.serialize_data()

    def serialize_data(self) -> None:
        '''
        Serializes the data into a pickle binary file.
        '''
        Path('StudentCalendars').mkdir(exist_ok=True)
        PickleSerializer.serialize_tuple_data(self._data, 'StudentCalendars/students_dump.pickle')


    def _parse_student_page(self):
        '''
        Helper method to parse the student's schedule page.
        '''
        parser = StudentYearPageParser(self._student_page)
        student_year_and_classes_data = parser.get_data()
        return student_year_and_classes_data

    def get_data(self):
        return self._data
