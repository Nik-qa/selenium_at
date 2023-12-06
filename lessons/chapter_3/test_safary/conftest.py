import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='chrome',
                     help="Choose browser: chrome or firefox or safari")
# если тут default='chrome' вместо 'chrome'  поставить None без кавычек, то будет ошибка

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, or safari")

    yield browser
    browser.quit()
    # для запуска с нужным бразуером pytest -s -v --browser_name=safari test_cmd.py