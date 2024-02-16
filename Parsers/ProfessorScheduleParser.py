from Domain.ProfessorClass import ProfessorClass
from Domain.ClassType import ClassType
from Domain.ClassType import get_class_type_from_str
from Domain.Frequency import Frequency
from Domain.Subject import Subject
from Parsers.BaseWebsiteParser import BaseWebsiteParser
from Domain.Frequency import get_frequency_from_string
from Domain.Room import Room


class ProfessorScheduleParserBase(BaseWebsiteParser):
    def __init__(self, given_url: str):
        '''
        Parser for professor's schedule.
        :param given_url: The url of the professor's schedule website.
        '''
        super().__init__(given_url)

    def get_data(self) -> list[ProfessorClass]:
        '''
        Parses the professor's schedule website using an xpath.
        :return: A list of ClassProfessor instances, what classes each professor has.
        '''
        self.get_browser()
        # xpath1 = for the table parses every line and gets all columns 1 through 8
        self._elements = self.get_elements_xpath("//table/tbody/tr[position() > 1]/td[position() <= 8]")
        # xpath2 = gets the header, which represents the professor name (format 'Orar TITLE NAME')
        output_list = [self.get_elements_xpath("//h1")[0].text]
        for index in range(0, len(self._elements), 8):
            day: str = self._elements[index].text
            # format of time on website: HH-HH
            start_hour, end_hour = self._elements[index + 1].text.split('-')
            frequency: Frequency = get_frequency_from_string(self._elements[index + 2].text)
            room: Room = Room(self._elements[index + 3].text, None)
            year: str = self._elements[index + 4].text
            formation: str = self._elements[index + 5].text
            class_type: ClassType = get_class_type_from_str(self._elements[index + 6].text)
            subject: Subject = Subject(self._elements[index + 7].text)
            individual_class = ProfessorClass(day, start_hour, end_hour, frequency, room, year, formation, class_type,
                                              subject)
            output_list.append(individual_class)

        return output_list
