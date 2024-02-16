from Repository.Repository import Repository
from Repository.PickleSerializer import PickleSerializer


class ProfessorSchedulePickleDumpRepository(Repository):
    def __init__(self):
        '''
        Repository for professor schedules. Populate data from pickle dump file
        '''
        super().__init__()
        self._data = self.deserialize_data()

    @staticmethod
    def deserialize_data():
        '''
        Deserialize data from pickle dump file
        '''
        return PickleSerializer.get_deserialized_data('ProfessorCalendars/professors_dump.pickle')

    def serialize_data(self):
        '''
        Serializes the data into a pickle binary file.
        '''
        PickleSerializer.serialize_tuple_data(self._data, 'ProfessorCalendars/professors_dump.pickle')

    def get_data(self):
        return self._data
