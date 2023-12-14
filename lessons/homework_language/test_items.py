import time
from selenium.webdriver.common.by import By


def test_check_button_add_product_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    buttons = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    time.sleep(10)
    # Проверка, что список не пустой
    assert len(buttons) > 0, "Кнопка не найдена на странице"

    # Получение текста первой найденной кнопки
    # text = buttons[0].text
     # assert "Добавить в корзину" == text


