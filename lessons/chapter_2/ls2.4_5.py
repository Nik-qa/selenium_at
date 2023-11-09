from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/wait1.html')

try:
    browser.implicitly_wait(5)
    browser.find_element(By.ID, 'verify').click()
    element = browser.find_element(By.ID,'verify_message')
    assert 'was' in element.text
finally:
    quit()

# задание 2.4_6 (закоментить код с 5 по 13, а строчки 16-17 раскомитить)
# browser.get('http://suninjuly.github.io/cats.html')
# browser.find_element(By.ID, "button").click()