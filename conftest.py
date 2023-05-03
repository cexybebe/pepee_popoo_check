import pytest
from selenium import webdriver


@pytest.fixture
def lang(request):
    return request.config.getoption("--language", default="en")


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..дадаядадая")
    user_language = request.config.getoption('language')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..опа!!!")
    browser.quit()
