import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


@pytest.fixture
def driver():
    # Setup: Create a WebDriver instance
    driver = webdriver.Chrome("C:\\Users\\Mavliutova Anzhela\\PycharmProjects\\pythonProject\\test_saucedemo\\chromedriver_win32\\chromedriver.exe")
    yield driver
    # Teardown: Quit the WebDriver instance
    driver.quit()


def test_login_valid_credentials(driver):
    # Instantiate the LoginPage
    login_page = LoginPage(driver)

    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Enter valid credentials
    login_page.login("standard_user", "secret_sauce")

    # Verify successful login by checking the presence of a specific element on the next page
    assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()


def test_login_invalid_credentials(driver):
    # Instantiate the LoginPage
    login_page = LoginPage(driver)

    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Enter invalid credentials
    login_page.login("invalid_user", "invalid_password")

    try:
        # Locate the error message element using CSS selector
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

        # Verify error message is displayed
        assert error_element.text == "Epic sadface: Username and password do not match any user in this service"
    except NoSuchElementException:
        # Handle the case when the error element is not found
        assert False, "Error message element not found"


