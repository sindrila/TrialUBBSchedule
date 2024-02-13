from Parsers.WebsiteParserInterface import WebsiteParserInterface
from Domain.Professor import get_name_from_title_and_name
from Domain.Professor import get_title_from_title_and_name
from Domain.Professor import Professor
from Parsers.ProfessorScheduleParser import ProfessorScheduleParser


class ProfessorPageParser(WebsiteParserInterface):

    def __init__(self, given_url: str):
        super().__init__(given_url)

    def get_data(self) -> list[tuple]:
        self.get_browser()
        self._elements = self.get_elements_xpath("//tbody//tr/td/a")
        professor_schedule_parser = ProfessorScheduleParser("")
        results = []
        print("Fetching professors and their schedules...")
        index = 0
        for element in self._elements:
            index += 1
            print(f"{index}/{len(self._elements)}")
            professor = Professor(get_name_from_title_and_name(element.text),
                                  get_title_from_title_and_name(element.text))
            try:
                assert (str(professor) == element.text)
            except AssertionError:
                raise Exception("Bad parsing. Expected professor " + element.text + " but parsed " + str(professor))

            professor_schedule_parser.url = element.get_attribute('href')

            professor_schedule = professor_schedule_parser.get_data()
            results.append((professor, professor_schedule))
        return results
