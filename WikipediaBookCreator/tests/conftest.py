__author__ = 'magic'

import pytest
from fixture.testapplication import TestApplication

@pytest.fixture(scope="session")
def app(request):
    browser = request.config.getoption("--browser")
    fixture = TestApplication(browser)
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
