from Domain.ClassType import ClassType
from Domain.Professor import Professor
from Domain.ClassProfessor import ClassProfessor
from Domain.Subject import Subject
from Domain.ClassType import get_class_type_from_str
from Parsers.ProfessorPageParser import ProfessorPageParser
from Domain.Professor import get_name_from_title_and_name
import re

from Parsers.ProfessorScheduleParser import ProfessorScheduleParser


def asserting(professor: Professor, professor_schedule_parser: ProfessorScheduleParser):
    current_professor_schedule = professor_schedule_parser.get_data()
    print(current_professor_schedule[2])
    try:
        assert (f"Orar {str(professor)}" == current_professor_schedule[0])
    except AssertionError:
        raise Exception(
            "Bad parsing. Expected professor " + current_professor_schedule[
                0] + " but parsed " + f"Orar {str(professor)}")


if __name__ == "__main__":
    test = ProfessorPageParser('https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/index.html')
    professors = test.get_data()

    asserting(professors[2][0], professors[2][1])
