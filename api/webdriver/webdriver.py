from selenium import webdriver


class Ocra:

    def get_browser(self):
        opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option("prefs", prefs)
        opt.add_argument('--headless')
        browser = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub', desired_capabilities=opt.to_capabilities())
        return browser


ocra = Ocra()