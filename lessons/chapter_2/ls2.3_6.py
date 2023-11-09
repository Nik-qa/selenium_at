from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    new_page = browser.window_handles[1]
    browser.switch_to.window(new_page)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

finally:
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    time.sleep(5)
    quit()


