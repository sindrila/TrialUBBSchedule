from enum import Enum


class Frequency(Enum):
    FIRST_WEEK = "sapt. 1"
    SECOND_WEEK = "sapt. 2"
    UNKNOWN = ""


FREQUNCY_MAPPING = {
    "sapt. 1": Frequency.FIRST_WEEK,
    "sapt. 2": Frequency.SECOND_WEEK
}


def get_frequency_from_string(string_frequency: str) -> Frequency:
    return FREQUNCY_MAPPING.get(string_frequency, Frequency.UNKNOWN)
