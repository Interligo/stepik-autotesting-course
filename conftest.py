import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: Chrome or Firefox.')
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language: ru, eng, etc.')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == 'firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=profile)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')
    yield browser
    browser.quit()
