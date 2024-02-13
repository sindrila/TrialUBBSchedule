from enum import Enum


class Faculty(Enum):
    INFORMATICA = "Informatica"
    MATEMATICA = "Matematica"
    MATEMATICA_INFORMATICA = "Matematica Informatica"
    INTELIGENTA_ARTIFICALA = "Inteligenta Artificala"
    INGINERIA_INFORMATIEI = "Ingineria Informatiei"
    PSIHOLOGIE = "Psihologie"
    BIOINFORMATICA = "Bioinformatica"
    UNKNOWN = ""


FACULTY_MAPPING = {
    "Informatica": Faculty.INFORMATICA,
    "Matematica": Faculty.MATEMATICA,
    "Matematica Informatica": Faculty.MATEMATICA_INFORMATICA,
    "Inteligenta Artificala": Faculty.INTELIGENTA_ARTIFICALA,
    "Ingineria Informatiei": Faculty.INGINERIA_INFORMATIEI,
    "Psihologie": Faculty.PSIHOLOGIE,
}


class LineOfStudy(Enum):
    ROMANA = "Romana"
    ENGLEZA = "Engleza"
    MAGHIARA = "Maghiara"
    UNKNOWN = ""


LINE_OF_STUDY_MAPPING = {
    "Romana": LineOfStudy.ROMANA,
    "Engleza": LineOfStudy.ENGLEZA,
    "Maghiara": LineOfStudy.MAGHIARA,
}


class YearOfStudy:
    def __init__(self, year: int, faculty: str, line_of_study: str):
        self._year = year
        self._faculty = FACULTY_MAPPING.get(faculty, Faculty.UNKNOWN)
        self._line_of_study = LINE_OF_STUDY_MAPPING.get(line_of_study, LineOfStudy.UNKNOWN)

    @property
    def year(self) -> int:
        return self._year

    @property
    def faculty(self) -> FACULTY_MAPPING:
        return self._faculty

    @property
    def line_of_study(self) -> LINE_OF_STUDY_MAPPING:
        return self._line_of_study

    @year.setter
    def year(self, year: int) -> None:
        self._year = year

    @faculty.setter
    def faculty(self, faculty: str) -> None:
        self._faculty = FACULTY_MAPPING.get(faculty, Faculty.UNKNOWN)

    @line_of_study.setter
    def line_of_study(self, line_of_study: str) -> None:
        self._line_of_study = LINE_OF_STUDY_MAPPING.get(line_of_study, LineOfStudy.UNKNOWN)

    def __str__(self):
        return f"{self.year} {self.faculty} - linia de studiu {self.line_of_study}"