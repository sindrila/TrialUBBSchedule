from enum import Enum


class ClassType(Enum):
    COURSE = "Curs"
    SEMINAR = "Seminar"
    LAB = "Laborator"
    UNKNOWN = "UNKOWN"


CLASS_TYPE_MAPPING = {
    "Curs": ClassType.COURSE,
    "Seminar": ClassType.SEMINAR,
    "Laborator": ClassType.LAB,
}


def get_class_type_from_str(class_type_string: str) -> ClassType:
    return CLASS_TYPE_MAPPING.get(class_type_string, ClassType.UNKNOWN)
