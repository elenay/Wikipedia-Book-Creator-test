__author__ = 'magic'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from create_book_helper import CreateBookHelper


class TestApplication():

    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.implicitly_wait(5)
        self.create_book = CreateBookHelper(self)
        self.base_url = "https://en.wikipedia.org/wiki/Main_Page"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_main_page(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def destroy(self):
        self.driver.quit()