import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://stepik.org/lesson/236895/step/1'


# @pytest.fixture(scope='function')
# def browser():
#     print("/nЗапуск браузера")
#     browser = webdriver.Chrome()
#     print("/Закрытие браузера")
#     yield browser
#     browser.quit()


def test_enter_to_account(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ember33'))
    )
    button.click()
    box = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'box-container'))
    )
    browser.find_element(By.ID, 'id_login_email').send_keys("badanov.n@yandex.ru")
    browser.find_element(By.ID, 'id_login_password').send_keys('Qaz1993$')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(3)

# box-container
