import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up():
    print('Start test')
    # url = 'https://www.saucedemo.com/'
    # options = webdriver.ChromeOptions()
    # #options.add_experimental_option('detach', True)
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(options=options, service=service)
    yield
    #driver.quit()
    print('Finish test')

@pytest.fixture(scope='module')
def set_group():
    print('Enter system')
    yield
    print('Exit system')