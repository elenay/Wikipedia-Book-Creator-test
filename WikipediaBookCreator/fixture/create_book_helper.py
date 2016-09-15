__author__ = 'magic'
import time
from time import strftime
import urllib


class CreateBookHelper:

    def __init__(self, app):
        self.app = app

    def click_create_book(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Create a book").click()

    def click_start_book_creator(self):
        driver = self.app.driver
        driver.find_element_by_name("confirm").click()

    def search_page(self, search_name):
        driver = self.app.driver
        searchbox = driver.find_element_by_id("searchInput")
        searchbox.send_keys(search_name)
        driver.find_element_by_id("searchButton").click()

    def add_page_to_book(self):
        driver = self.app.driver
        time.sleep(3)
        driver.find_element_by_id("coll-add_article").click()

    def show_book(self):
        driver = self.app.driver
        driver.find_element_by_partial_link_text("Show book").click()

    def set_book_name_and_subtitle(self):
        driver = self.app.driver
        time.sleep(3)
        driver.find_element_by_id("titleInput").send_keys("Book Creator from Wikipedia")
        driver.find_element_by_id("subtitleInput").send_keys("Using Automation")

    def press_download_book(self):
        driver = self.app.driver
        driver.find_element_by_id("downloadButton").click()

    def download_to_computer(self):
        driver = self.app.driver
        url = driver.find_element_by_link_text("Download the file").get_attribute("href")
        timestamp = strftime("%Y-%m-%d_%H-%M-%S")
        file_name = '..\\Exported_Book_'+timestamp+'.pdf'
        pdf_file = urllib.urlretrieve(url, file_name)
        return file_name



