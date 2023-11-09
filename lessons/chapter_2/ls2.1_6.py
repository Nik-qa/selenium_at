from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_x = browser.find_element(By.ID, 'input_value')
    x = find_x.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID,'robotCheckbox')
    check_checkbox = checkbox.get_attribute('checked')
    assert check_checkbox is None # проверяет что его нет 'is None' - нет ничего, т.е. нет атрибута
    checkbox.click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(1)
    browser.quit()

