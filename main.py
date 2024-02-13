from Domain.Professor import Professor
from Parsers.ProfessorPageParser import ProfessorPageParser
import pickle


def assert_professor_schedule(professor: Professor, current_professor_schedule: list):
    try:
        assert (f"Orar {str(professor)}" == current_professor_schedule[0])
    except AssertionError:
        raise Exception(
            "Bad parsing. Expected professor " + current_professor_schedule[
                0] + " but parsed " + f"Orar {str(professor)}")


def serialize_tuple_professor_and_classes(data) -> None:
    with open('professors_dump.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_deserialized_tuple_professor_and_classes():
    with open('professors_dump.pickle', 'rb') as handle:
        return pickle.load(handle)


def parse_professor_page():
    parser = ProfessorPageParser('https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/index.html')
    professors_and_classes_data = parser.get_data()
    for professor_schedule in professors_and_classes_data:
        assert_professor_schedule(professor_schedule[0], professor_schedule[1])
    return professors_and_classes_data


if __name__ == "__main__":
    professors_and_classes = get_deserialized_tuple_professor_and_classes()
