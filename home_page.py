from selenium.webdriver.common.by import By

class HomePage:
    # Locators
    PRODUCT_LABEL = (By.CLASS_NAME, "product_label")

    def __init__(self, driver):
        self.driver = driver

    def get_product_label_text(self):
        return self.driver.find_element(*self.PRODUCT_LABEL).text
