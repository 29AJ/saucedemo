import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage


@pytest.fixture
def logged_in_driver():
    # Setup: Create a WebDriver instance
    driver_path = (
        "C:\\Users\\Mavliutova Anzhela\\PycharmProjects\\pythonProject\\"
        "test_saucedemo\\chromedriver_win32\\chromedriver.exe"
    )
    driver = webdriver.Chrome(driver_path)

    # Instantiate the LoginPage
    login_page = LoginPage(driver)

    # Navigate to the login page
    login_page.go_to_login_page()
    login_page.login("standard_user", "secret_sauce")

    # Yield the logged-in driver to the test
    yield driver

    # Teardown: Quit the WebDriver instance
    driver.quit()


def test_add_and_delete_product_from_cart(logged_in_driver):
    driver = logged_in_driver

    # After successful login, navigate to the inventory page
    home_page = HomePage(driver)

    # Add products to cart
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for product_name in products_to_add:
        home_page.add_product_to_cart(product_name)
        print(f"Added product '{product_name}' to cart")

    # Verify products are added to cart
    cart_page = CartPage(driver)
    cart_page.open()
    cart_items = cart_page.get_cart_items()
    print("Cart items:", cart_items)  # Print the cart items
    print("Expected cart items:", products_to_add)  # Print the expected cart items
    assert len(cart_items) == len(products_to_add), \
        f"Expected {len(products_to_add)} items in cart, but found {len(cart_items)}"

    # Delete a product from the cart
    product_to_delete = "Sauce Labs Bike Light"
    cart_page.delete_product_from_cart(product_to_delete)

    # Verify the product is no longer in the cart
    cart_items = cart_page.get_cart_items()
    assert product_to_delete not in cart_items, f"Product '{product_to_delete}' still found in the cart"
