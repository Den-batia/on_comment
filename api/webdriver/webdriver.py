from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Ocra:

    def get_browser(self):
        browser = webdriver.Remote('http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        return browser


ocra = Ocra()