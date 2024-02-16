import pickle


class PickleSerializer:
    @staticmethod
    def serialize_tuple_data(data, file_name) -> None:
        '''
        Helper method to serialize data into a pickle binary file.
        '''
        with open(file_name, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_deserialized_data(file_name):
        '''
        Helper method to deserialize data from a pickle binary file.
        '''
        with open(file_name, 'rb') as handle:
            return pickle.load(handle)
