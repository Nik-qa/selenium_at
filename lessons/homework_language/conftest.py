import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='chrome',
                     help="Choose browser: chrome or firefox or safari")
    parser.addoption("--language", action="store", default=None,
                     help="Choose language: e.g., en, es, fr, etc.")
    parser.addoption("--headless", action="store_true",
                     help="Run the browser in headless mode")
# если тут default='chrome' вместо 'chrome'  поставить None без кавычек, то будет ошибка


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    headless_mode = request.config.getoption("headless")

    options = Options()
    if user_language:
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if headless_mode:
        options.add_argument("--headless")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, or safari")

    yield browser
    print("\nquit browser..")
    browser.quit()
# для запуска с нужным бразуером pytest -s -v --browser_name=safari test_cmd.py