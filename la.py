from selenium import webdriver
import time

# Page Object Model (POM) for the login page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id("user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id("login-button").click()

# Page Object Model (POM) for the product list page
class ProductListPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):
        product_elements = self.driver.find_elements_by_class_name("inventory_item_name")
        product_names = [element.text for element in product_elements]
        return product_names

# Set the path to the ChromeDriver executable
driver_path = 'path/to/chromedriver'  # Replace with the actual path to chromedriver.exe

# Create an instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Start measuring performance
start_time = time.time()

# Open the Sauce Demo website
driver.get("https://www.saucedemo.com/")

# Perform login
login_page = LoginPage(driver)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# Verify the product list page
product_list_page = ProductListPage(driver)
product_names = product_list_page.get_product_names()
print("Product names:", product_names)

# End measuring performance
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)

# Close the browser
driver.quit
