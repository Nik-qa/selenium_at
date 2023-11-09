from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_elements(By.TAG_NAME, 'input')
    for element in element:
        element.send_keys("1")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()