from Domain.ClassType import ClassType
from Domain.Professor import Professor
from Domain.ClassProfessor import ClassProfessor
from Domain.Subject import Subject
from Parsers.CadreDidacticeParser import CadreDidacticeParser
from Domain.ClassType import get_class_type_from_str
from Parsers.ProfessorScheduleParser import ProfessorScheduleParser
from Domain.Professor import extract_whole_name_from_header
import re
def professor_from_whole_name_to_professor_header(header: str):
    pattern = r'.*\b*.\b'

    # Search for the pattern in the header
    match = re.search(pattern, header)
    # If a match is found, return the matched text
    if match:
        return match.group(0)
    else:
        return ''  # Return an empty string if no match is found
    title = header.split(' ')[0]
    print(title)
    name = header.split(' ')[-1:]
    print(name)
    # if len(whole_name) == 2:
    #     return Professor(whole_name.split(' ')[0], whole_name.split(' ')[1], )
    # return Professor


if __name__ == "__main__":
    test = ProfessorScheduleParser('https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/vege.html')
    schedule = test.get_text()
    professor_from_whole_name_to_professor_header(schedule[0])
    # whole_name = extract_whole_name_from_header(schedule[0])
    # professor = Professor(whole_name.split([0], whole_name)
    for indiviudal_class in schedule:
        print(indiviudal_class)
    # print(len(test))

    # test_schedule = ClassProfessor("Luni", 12, 14, "", "Multimedia", "3 Info engleza", "512", get_class_type_from_str("Laborator"), Subject("Proiect colectiv"), Professor("Karoly", "", "SIMON", "Lect."))
    # print(test_schedule)
