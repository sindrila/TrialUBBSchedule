from enum import Enum
import re


class ProfessorTitle(Enum):
    ASISTENT = "Asist."
    CADRU_DIDACTIC_ASOCIAT = "C.d.asociat"
    LECTOR = "Lect."
    CONFERENTIAR = "Conf."
    DOCTOR = "Drd."
    PROFESOR = "Prof."
    UNKNOWN = ""


TITLE_MAPPING = {
    "Asist.": ProfessorTitle.ASISTENT,
    "C.d.asociat": ProfessorTitle.CADRU_DIDACTIC_ASOCIAT,
    "C.": ProfessorTitle.CADRU_DIDACTIC_ASOCIAT,
    "Lect.": ProfessorTitle.LECTOR,
    "Conf.": ProfessorTitle.CONFERENTIAR,
    "Drd.": ProfessorTitle.DOCTOR,
    "Prof.": ProfessorTitle.PROFESOR,
}


def get_title_from_title_and_name(title_and_name: str) -> ProfessorTitle:
    pattern = r'\w+\.'
    match = re.search(pattern, title_and_name)
    return TITLE_MAPPING.get(match.group(), ProfessorTitle.UNKNOWN)


def get_name_from_title_and_name(title_and_name: str) -> str:
    if title_and_name == "Drd. DoctorandM":
        return "DoctorandM"
    if title_and_name == "Drd. Doctorand Info":
        return "Doctorand Info"
    if title_and_name == "Drd. Orzan Alexandru":
        return "Orzan Alexandru"
    if title_and_name == "C.d.asociat Coste Monica":
        return "Coste Monica"

    pattern = r'[A-Z]{2,}.*$'
    match = re.search(pattern, title_and_name)
    if match:
        return match.group()
    else:
        return ''


class Professor:
    def __init__(self, name: str, title: str) -> None:
        self._name = name
        self._title: ProfessorTitle = title

    @property
    def name(self) -> str:
        return self._name

    @property
    def title(self) -> str:
        return self._title.value

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @title.setter
    def title(self, string_title: str) -> None:
        self._title = get_title_from_title_and_name(string_title)

    def __str__(self):
        return self.title + ' ' + self.name
