from Domain.ClassProfessor import ClassProfessor
from Domain.ClassType import ClassType
from Domain.ClassType import get_class_type_from_str
from Domain.Frequency import Frequency
from Domain.Subject import Subject
from Parsers.WebsiteParserInterface import WebsiteParserInterface
from Domain.Frequency import get_frequency_from_string
from Domain.Room import Room


class ProfessorScheduleParser(WebsiteParserInterface):
    def __init__(self, given_url: str):
        super().__init__(given_url)
        self._elements = self.get_elements_xpath("//table/tbody/tr[position() > 1]/td[position() <= 8]")

    # def get_list_of_classes(self):

    def get_text(self):
        output_list = [self.get_elements_xpath("//h1")[0].text]
        for index in range(0, len(self._elements), 8):
            # for j in range(index, index + 8):
            #     print(self._elements[j].text)
            day: str = self._elements[index].text
            start_hour, end_hour = self._elements[index + 1].text.split('-')
            frequency: Frequency = get_frequency_from_string(self._elements[index + 2].text)
            room: Room = Room(self._elements[index + 3].text, None)
            year: str = self._elements[index + 4].text
            formation: str = self._elements[index + 5].text
            class_type: ClassType = get_class_type_from_str(self._elements[index + 6].text)
            subject: Subject = Subject(self._elements[index + 7].text)
            individual_class = ClassProfessor(day, start_hour, end_hour, frequency, room, year, formation, class_type,
                                              subject)
            output_list.append(individual_class)

        return output_list
