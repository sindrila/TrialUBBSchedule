from selenium.webdriver.common.by import By

from Parsers.WebsiteParserInterface import WebsiteParserInterface


class CadreDidacticeParser(WebsiteParserInterface):
    def __init__(self, given_url : str):
        super().__init__(given_url)
        self._elements = []
        self.find_elements_xpath("//tbody//a")

    def find_elements_xpath(self, xpath: str):
        self._elements = self._browser.find_elements(By.XPATH, xpath)

    def get_text(self):
        '''
        Gets teachers' names.
        :return: list of strings
        '''
        all_teachers = []
        for element in self._elements:
            all_teachers.append(element.text)
        return all_teachers

    def get_website(self):
        '''
        Gets teachers' schedule website.
        :return:  list of strings
        '''
        all_addresses = []
        for element in self._elements:
            all_addresses.append(element.get_attribute('href'))
        return all_addresses

    def get_tuple_text_website(self):
        '''
        Gets teachers' schedule website and name,'
        :return: list of tuples [(name, website), ...]
        '''
        all_data = []
        for element in self._elements:
            all_data.append((element.text, element.get_attribute('href')))
        return all_data

