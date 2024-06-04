import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Select default browser language")


@pytest.fixture
def user_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(user_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
