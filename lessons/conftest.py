import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope='function')
def browser():
    print("/nЗапуск браузера для тестов..")
    browser = webdriver.Chrome()
    yield browser
    print("/nЗакрываем браузер..")
    browser.quit()
