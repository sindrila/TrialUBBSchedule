from Parsers.BaseWebsiteParser import BaseWebsiteParser
from Domain.Professor import get_name_from_title_and_name
from Domain.Professor import get_title_from_title_and_name
from Domain.Professor import Professor
from Parsers.ProfessorScheduleParser import ProfessorSchedulePageParser


class ProfessorPageParser(BaseWebsiteParser):

    def __init__(self, given_url: str):
        super().__init__(given_url)
        '''
        Parser for professor's names.
        :param given_url: The url of the list of professor's schedules website.
        '''

    def get_data(self) -> list[tuple]:
        '''
        Parses professor's schedules website using an xpath.
        :return: A list of tuples containing professor's names and titles and their schedule's url.
        '''
        self.get_browser()

        # xpath = gets all <a> tags from a table
        self._elements = self.get_elements_xpath("//tbody//tr/td/a")
        professor_schedule_parser = ProfessorSchedulePageParser("")
        results = []
        print("Fetching professors and their schedules...")
        index = 0
        for element in self._elements:
            index += 1
            print(f"{index}/{len(self._elements)}")
            # creates Professor instance with the name and title extracted.
            professor = Professor(get_name_from_title_and_name(element.text),
                                  get_title_from_title_and_name(element.text))

            professor_schedule_parser.url = element.get_attribute('href')
            professor_schedule = professor_schedule_parser.get_data()
            results.append((professor, professor_schedule))
        return results
