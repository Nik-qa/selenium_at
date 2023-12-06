import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox or safari")

@pytest.fixture(scope='function')
def test_launch_safari(browser):
    link = ('https://stepik.org/lesson/25969/step/8')
    browser.get(link)