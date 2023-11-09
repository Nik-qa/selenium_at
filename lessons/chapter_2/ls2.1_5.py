from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    fild = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    fild.send_keys(y)

    browser.find_element(By.CLASS_NAME, 'form-check-label').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(2)
    browser.quit()
