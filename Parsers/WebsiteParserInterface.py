from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By


class WebsiteParserInterface(ABC):
    def __init__(self, given_url: str):
        self._url = given_url
        self._browser = None
        self._elements = []

        web_driver_options = Options()
        web_driver_options.add_argument("--headless")
        self._browser: webdriver.Firefox = webdriver.Firefox(options=web_driver_options)

    def get_browser(self):
        self._browser.get(self._url)

    @abstractmethod
    def get_data(self):
        pass

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def __del__(self):
        self._browser.quit()

    def get_elements_xpath(self, xpath: str):
        return self._browser.find_elements(By.XPATH, xpath)
