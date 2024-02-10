from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebsiteParserInterface:
    def __init__(self, given_url: str):
        self._url = given_url
        # self._webdriver = webdriver.Firefox()
        web_driver_options = Options()
        web_driver_options.add_argument("--headless")
        self._browser = webdriver.Firefox(options=web_driver_options)
        self._browser.get(self._url)

    def __del__(self):
        self._browser.close()

    def get_text(self):
        pass

    def get_website(self):
        pass

    def get_tuple_text_website(self):
        pass
