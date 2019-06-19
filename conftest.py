import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
