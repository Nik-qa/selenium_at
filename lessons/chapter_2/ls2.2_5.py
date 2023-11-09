from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    time.sleep(2)
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) либо вниже двигаем на 300 пикселей
    browser.execute_script('window.scrollBy(0, 300);')
    button.click()

finally:
    time.sleep(2)
    quit()
