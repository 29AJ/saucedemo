from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select


class HomePage:
    # Locators for product elements
    PRODUCT = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_primary")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def get_sort_select(self):
        return Select(self.driver.find_element(*self.SORT_SELECT))

    def select_sort_option(self, option_value):
        sort_select = self.get_sort_select()
        sort_select.select_by_value(option_value)

    def get_product_prices(self):
        product_prices = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [price.text for price in product_prices]

    def add_product_to_cart(self, product_name):
        product_elements = self.driver.find_elements(*self.PRODUCT)
        print("Number of product elements found:", len(product_elements))

        wait = WebDriverWait(self.driver, 10)  # Create a WebDriverWait instance with a timeout of 10 seconds

        for element in product_elements:
            name_element = element.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text.strip() == product_name:
                add_to_cart_button = wait.until(
                    expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn_primary"))
                )
                print(f"Adding product to cart: {product_name}")
                add_to_cart_button.click()
                print("Clicked 'Add to Cart' button")
                break
        else:
            print(f"Product '{product_name}' not found on the page")
