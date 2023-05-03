import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..дадаядадая")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..опа!!!")
    browser.quit()
