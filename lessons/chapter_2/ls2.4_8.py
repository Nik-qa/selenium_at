from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time, math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        ES.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    browser.execute_script('window.scrollBy(0, 300);')
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    time.sleep(2)
    quit()

