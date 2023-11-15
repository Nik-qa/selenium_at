from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block :nth-child(2) .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    input3.send_keys("Smolensk")
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    quit()