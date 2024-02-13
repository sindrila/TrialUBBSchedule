from Repository.Repository import Repository
from PickleSerializer import PickleSerializer


class ProfessorSchedulePickleDumpRepository(Repository):
    def __init__(self):
        super().__init__()
        self._data = self.deserialize_data()

    @staticmethod
    def deserialize_data():
        return PickleSerializer.get_deserialized_data('ProfessorCalendars/professors_dump.pickle')

    def serialize_data(self):
        PickleSerializer.serialize_tuple_data(self._data, 'ProfessorCalendars/professors_dump.pickle')

    def get_data(self):
        return self._data
