from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    answer = browser.find_element(By.ID, 'input_value')
    x = answer.text
    y = calc(x)
    fild = browser.find_element(By.ID, 'answer')
    fild.send_keys(y)

    browser.execute_script('window.scrollBy(0, 250);')
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(3)
    quit()

