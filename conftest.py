import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language',
                    action='store', 
                    default='en',
                    help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    browser = None
    if lang == "ru":
        print("\nstart chrome browser for ru test..")
    elif lang == "en":
        print("\nstart chrome browser for en test..")
    else:
        raise pytest.UsageError("--languge should be ru or en")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
