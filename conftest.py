import pytest
from selenium import webdriver


@pytest.fixture
def lang(request):
    return request.config.getoption("--lang", default="en")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..дадаядадая")
    browser = webdriver.Safari()
    yield browser
    print("\nquit browser..опа!!!")
    browser.quit()
