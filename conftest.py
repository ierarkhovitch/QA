import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()
