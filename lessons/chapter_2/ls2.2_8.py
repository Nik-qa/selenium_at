from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys("lol")
    browser.find_element(By.NAME, 'lastname').send_keys("lol")
    browser.find_element(By.NAME, 'email').send_keys("lol@gmail.com")

    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print('current_dir', current_dir)
    file_path = os.path.join(current_dir, 'file.txt')
    print('file_path', file_path)

    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    time.sleep(3)
    quit()