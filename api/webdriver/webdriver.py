from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Ocra:
    browser = None

    def init_browser(self):
        if not self.browser:
            self.browser = webdriver.Remote('http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
            return self.browser
        else:
            return None

    def quite_browser(self):
        if self.browser:
            self.browser.quit()
            self.browser = None


ocra = Ocra()