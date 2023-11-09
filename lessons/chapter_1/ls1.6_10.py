from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CLASS_NAME, 'form-control')
    name.send_keys("Ni")
    browser.find_element(By.CLASS_NAME, 'second').send_keys('Smith')
    browser.find_element(By.CLASS_NAME, 'third').send_keys('Moscow@gm.com')
    browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys('89001230090')
    browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('123')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()