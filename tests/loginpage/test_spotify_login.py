import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LogInPage
from pages.common.header_section import HeaderSection

@pytest.fixture()
def browser():
    driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid(browser):
    # Initialize the pages
    login_page = LogInPage(browser)
    header = HeaderSection(browser)

    # Navigate to the spotify
    login_page.navigate(login_page.config.get('APP', 'url'))

    # Click on the login button
    header.click_login_btn()

    # Login with valid credentials 
    is_logged_in = login_page.login_with_email(
        login_page.config.get('CREDENTIALS', 'username'),
        login_page.config.get('CREDENTIALS', 'password'))
    
    # Verify successful login
    assert is_logged_in == True
    

@pytest.mark.parametrize('username,password', [
    ('', 'password1'),
    ('user1', ''),
    ('', '')
])
def test_login_invalid(browser, username, password):

    login_page = LogInPage(browser)
    header = HeaderSection(browser)

    # Navigate to the spotify
    login_page.navigate(login_page.config.get('APP', 'url'))

    # Click on the login button
    header.click_login_btn()

    # Login with valid credentials 
    is_logged_in = login_page.login_with_email(username, password)
    
    # Verify successful login
    assert is_logged_in == False
    

    # Verify the error message
    assert login_page.validate_error_message('Incorrect username or password.') == True