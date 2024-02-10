from enum import Enum


class ProfessorTitle(Enum):
    ASISTENT = "Asist."
    CADRU_DIDACTIC_ASOCIAT = "C.d. asociat"
    LECTOR = "Lect."
    CONFERENTIAR = "Conf."
    DOCTOR = "Dr."
    PROFESOR = "Prof."
    UNKNOWN = ""


TITLE_MAPPING = {
    "Asist.": ProfessorTitle.ASISTENT,
    "C.d. asociat": ProfessorTitle.CADRU_DIDACTIC_ASOCIAT,
    "Lect.": ProfessorTitle.LECTOR,
    "Conf.": ProfessorTitle.CONFERENTIAR,
    "Dr.": ProfessorTitle.DOCTOR,
    "Prof.": ProfessorTitle.PROFESOR,
}


def get_title_from_string(string_title: str) -> ProfessorTitle:
    return TITLE_MAPPING.get(string_title, ProfessorTitle.UNKNOWN)


class Professor:
    def __init__(self, given_name: str, middle_name: str, family_name: str, title: str) -> None:
        self._given_name = given_name
        self._middle_name = middle_name
        self._family_name = family_name
        self._title = get_title_from_string(title)

    @property
    def given_name(self) -> str:
        return self._given_name

    @property
    def middle_name(self) -> str:
        return self._middle_name

    @property
    def family_name(self) -> str:
        return self._family_name

    @property
    def title(self) -> str:
        return self._title

    @family_name.setter
    def family_name(self, family_name: str) -> None:
        self._family_name = family_name

    @given_name.setter
    def given_name(self, given_name: str) -> None:
        self._given_name = given_name

    @middle_name.setter
    def middle_name(self, middle_name: str) -> None:
        self._middle_name = middle_name

    @title.setter
    def title(self, string_title: str) -> None:
        self._title = get_title_from_string(string_title)
