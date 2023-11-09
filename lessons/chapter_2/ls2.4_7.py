from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/wait1.html')

try:
    button = WebDriverWait(browser, 5).until(
        ES.element_to_be_clickable((By.ID, 'verify'))
    )
    button.click()
    message = browser.find_element(By.ID,'verify_message')
    assert 'was' in message.text
finally:
    quit()