import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NE
import time
import math




@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1"])
# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
#                                   'https://stepik.org/lesson/236896/step/1',
#                                   "https://stepik.org/lesson/236897/step/1",
#                                   'https://stepik.org/lesson/236898/step/1',
#                                   'https://stepik.org/lesson/236899/step/1',
#                                   'https://stepik.org/lesson/236903/step/1',
#                                   'https://stepik.org/lesson/236904/step/1',
#                                   'https://stepik.org/lesson/236905/step/1'])
def test_enter_to_account(browser, link):
    # авторизация
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'ember33'))
    )
    button.click()
    box = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'box-container'))
    )
    browser.find_element(By.ID, 'id_login_email').send_keys("badanov.n@yandex.ru")
    browser.find_element(By.ID, 'id_login_password').send_keys('Qaz1993$')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()

    # инпут и отправка
    # ищем кнопку
    try:
        answer = math.log(int(time.time()))
        time.sleep(5)
        input = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        input.send_keys(answer)
        time.sleep(5)
        send = browser.find_element(By.CLASS_NAME, 'submit-submission')
        send.click()

        time.sleep(3)
        again = browser.find_element(By.CLASS_NAME, "again-btn")
        again.click()

    finally:

        time.sleep(3)
#     again-btn white


