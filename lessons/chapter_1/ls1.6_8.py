from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link='http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CLASS_NAME, 'form-control')
    name.send_keys("Ni")
    browser.find_element(By.NAME, 'last_name').send_keys('Smith')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Moscow')
    browser.find_element(By.ID, 'country').send_keys('Russia')
    button = browser.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
