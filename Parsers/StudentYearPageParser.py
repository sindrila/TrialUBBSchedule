from Parsers.BaseWebsiteParser import BaseWebsiteParser
from Parsers.StudentYearScheduleParser import StudentYearScheduleParser


class StudentYearPageParser(BaseWebsiteParser):
    def __init__(self, given_url: str):
        '''
        Parser for student's schedule page.
        :param given_url: The url of schedule for all student years page.
        '''
        super().__init__(given_url)

    def get_data(self) -> list[tuple]:
        '''
        Parses student's schedules website using an xpath.
        :return: A list of tuples containing specialization and year abbreviated, and the corresponding schedule url.
        '''
        self.get_browser()

        # xpath = gets all <a> tags from a table
        self._elements = self.get_elements_xpath("//tbody//tr/td/a")
        student_schedule_parser = StudentYearScheduleParser("")
        results = []
        print("Fetching specializations and their schedules...")
        index = 0

        for element in self._elements:
            index += 1
            print(f"{index}/{len(self._elements)}")
            year = element.get_attribute('href').split('/tabelar/')[1].split('.html')[0]

            student_schedule_parser.url = element.get_attribute('href')
            student_schedule = student_schedule_parser.get_data()
            results.append((year, student_schedule))

        return results
