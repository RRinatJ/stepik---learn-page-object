import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):    
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en or etc")    

    
@pytest.fixture(scope="function")
def browser(request):   
    language = request.config.getoption("language")    
    browser = None
    if not language:
        language = "en"
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})        
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)   
    
    yield browser
    print("\nquit browser..")
    browser.quit()