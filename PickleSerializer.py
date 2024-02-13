import pickle


class PickleSerializer:
    @staticmethod
    def serialize_tuple_data(data, file_name) -> None:
        with open(file_name, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_deserialized_data(file_name):
        with open(file_name, 'rb') as handle:
            return pickle.load(handle)
