import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        product_label_text = home_page.get_product_label_text()

        self.assertEqual(product_label_text, "Products", "Login failed")

if __name__ == "__main__":
    unittest.main()
