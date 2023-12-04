import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nЗапуска браузера..")
    browser = webdriver.Chrome()
    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()
