import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


@pytest.fixture
def driver():
    # Setup: Create a WebDriver instance
    driver_path = (
        "C:\\Users\\Mavliutova Anzhela\\PycharmProjects\\pythonProject\\"
        "test_saucedemo\\chromedriver_win32\\chromedriver.exe"
    )
    driver = webdriver.Chrome(driver_path)
    yield driver
    # Teardown: Quit the WebDriver instance
    driver.quit()


def test_product_sorting(driver):
    # Instantiate the LoginPage
    login_page = LoginPage(driver)

    # Navigate to the login page
    login_page.go_to_login_page()

    # Login with valid credentials
    login_page.login("standard_user", "secret_sauce")

    # Instantiate the HomePage
    home_page = HomePage(driver)

    # Open the homepage with the product list
    home_page.open()

    # Get the select element for sorting
    sort_select = home_page.get_sort_select()

    # Verify the default sorting option
    default_option = sort_select.first_selected_option.text
    assert default_option == "Name (A to Z)", "Default sorting option is incorrect"

    # Select the "Price (low to high)" option
    home_page.select_sort_option("lohi")

    # Get the list of product prices
    product_prices = home_page.get_product_prices()

    # Convert the product prices to numeric values
    prices = [float(price.strip("$")) for price in product_prices]

    # Check if the prices are sorted in ascending order
    assert prices == sorted(prices), "Product prices are not sorted in ascending order"

    # Select the "Price (high to low)" option
    home_page.select_sort_option("hilo")

    # Get the list of product prices again
    product_prices = home_page.get_product_prices()

    # Convert the product prices to numeric values again
    prices = [float(price.strip("$")) for price in product_prices]

    # Check if the prices are sorted in descending order
    assert prices == sorted(prices, reverse=True), "Product prices are not sorted in descending order"
