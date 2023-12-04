from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link1 = 'https://stepik.org/lesson/236895/step/1'
browser = webdriver.Chrome()
answer = math.log(int(time.time()))

try:
    browser.get(link1)
    browser.get("https://stepik.org/lesson/236895/step/1")
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
    time.sleep(2)
    input = browser.find_element(By.CLASS_NAME, 'ember-text-area')
    input.send_keys(answer)
    button2 = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
# class="attempt-message_correct"
# class ="smart-hints__hint"
