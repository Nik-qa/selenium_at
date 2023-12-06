import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox or safari")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    # browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, or safari")

    yield browser
    browser.quit()