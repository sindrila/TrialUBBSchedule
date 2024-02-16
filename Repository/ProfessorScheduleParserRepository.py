from Repository.PickleSerializer import PickleSerializer
from Domain.Professor import Professor
from Parsers.ProfessorPageParser import ProfessorPageParserBase
from Repository.Repository import Repository


class ProfessorScheduleParserRepository(Repository):
    def __init__(self, professor_page: str = 'https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/index.html'):
        '''
        Repository for professor schedules. Populates data by parsing.
        :param professor_page: URL of professor schedules page
        '''
        super().__init__()
        self._professor_page: str = professor_page
        self._data = self._parse_professor_page()
        self.serialize_data()

    @staticmethod
    def _assert_professor_schedule(professor: Professor, current_professor_schedule: list) -> None:
        '''
        Checks if the professor schedule is valid.
        current_professor_schedule[0] = header of the professor page Orar TITLE NAME
        '''
        try:
            assert (f"Orar {str(professor)}" == current_professor_schedule[0])
        except AssertionError:
            raise Exception(
                "Bad parsing. Expected professor " + current_professor_schedule[
                    0] + " but parsed " + f"Orar {str(professor)}")

    def serialize_data(self) -> None:
        '''
        Serializes the data into a pickle binary file.
        '''
        PickleSerializer.serialize_tuple_data(self._data, 'ProfessorCalendars/professors_dump.pickle')

    def _parse_professor_page(self):
        '''
        Helper method to parse the professor schedule page.
        '''
        parser = ProfessorPageParserBase(self._professor_page)
        professors_and_classes_data = parser.get_data()
        for professor_schedule in professors_and_classes_data:
            self._assert_professor_schedule(professor_schedule[0], professor_schedule[1])
        return professors_and_classes_data

    def get_data(self):
        return self._data
