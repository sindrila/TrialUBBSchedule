from PickleSerializer import PickleSerializer
from Domain.Professor import Professor
from Parsers.ProfessorPageParser import ProfessorPageParser
from Repository.Repository import Repository


class ProfessorScheduleParserRepository(Repository):
    def __init__(self, professor_page: str = 'https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/index.html'):
        super().__init__()
        self._professor_page: str = professor_page
        self._data = self._parse_professor_page()
        self.serialize_data()

    @staticmethod
    def _assert_professor_schedule(professor: Professor, current_professor_schedule: list):
        try:
            assert (f"Orar {str(professor)}" == current_professor_schedule[0])
        except AssertionError:
            raise Exception(
                "Bad parsing. Expected professor " + current_professor_schedule[
                    0] + " but parsed " + f"Orar {str(professor)}")

    def serialize_data(self):
        PickleSerializer.serialize_tuple_data(self._data, 'ProfessorCalendars/professors_dump.pickle')

    def _parse_professor_page(self):
        parser = ProfessorPageParser(self._professor_page)
        professors_and_classes_data = parser.get_data()
        for professor_schedule in professors_and_classes_data:
            self._assert_professor_schedule(professor_schedule[0], professor_schedule[1])
        return professors_and_classes_data

    def get_data(self):
        return self._data
