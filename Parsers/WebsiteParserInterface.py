from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
class WebsiteParserInterface(ABC):
    def __init__(self, given_url: str):
        self._url = given_url
        # self._webdriver = webdriver.Firefox()
        web_driver_options = Options()
        web_driver_options.add_argument("--headless")
        self._browser = webdriver.Firefox(options=web_driver_options)
        self._browser.get(self._url)

    def __del__(self):
        self._browser.close()

    @abstractmethod
    def get_text(self):
        pass
    
    def get_elements_xpath(self, xpath: str):
        return self._browser.find_elements(By.XPATH, xpath)
