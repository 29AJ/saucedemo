from selenium.webdriver.common.by import By

class CartPage:
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def get_cart_items(self):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        print("Number of cart items found:", len(cart_items))
        cart_item_texts = [item.text for item in cart_items]
        print("Cart items:", cart_item_texts)  # Print the cart items
        return cart_item_texts

    def delete_product_from_cart(self, product_name):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        for item in cart_items:
            if product_name in item.text:
                remove_button = item.find_element(*self.REMOVE_BUTTON)
                remove_button.click()
                break



