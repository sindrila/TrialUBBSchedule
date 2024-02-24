from Repository.PickleSerializer import PickleSerializer
from Repository.Repository import Repository


class StudentSchedulePickleDumpRepository(Repository):
    def __init__(self):
        '''
        Repository for student schedules. Populate data form pickle dump file.
        '''
        super().__init__()
        self._data = self.deserialize_data()

    @staticmethod
    def deserialize_data():
        '''
        Deserialize data from pickle dump file
        '''
        return PickleSerializer.get_deserialized_data('StudentCalendars/students_dump.pickle')

    def serialize_data(self) -> None:
        '''
        Serializes the data into a pickle binary file.
        '''
        PickleSerializer.serialize_tuple_data(self._data, 'StudentCalendars/students_dump.pickle')

    def get_data(self):
        return self._data