__author__ = 'magic'
import os.path


def test_create_wiki_book(app):
    app.open_main_page()
    app.create_book.click_create_book()
    app.create_book.click_start_book_creator()
    app.create_book.search_page("Selenium")
    app.create_book.add_page_to_book()
    app.create_book.search_page("JScript")
    app.create_book.add_page_to_book()
    app.create_book.show_book()
    app.create_book.set_book_name_and_subtitle()
    app.create_book.press_download_book()
    file_name = app.create_book.download_to_computer()
    assert os.path.isfile(file_name)
    assert os.path.getsize(file_name) > 0