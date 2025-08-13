from selenium.webdriver import Chrome
from pages.login_page import LoginPage
class TestLogin():
    def test_login_valid(self):
        driver = Chrome()
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user","secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    def test_login_invalid(self):
        driver = Chrome()
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user","secret_sauce123")
        assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"