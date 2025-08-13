from selenium.webdriver import Chrome
from pages.login_page import LoginPage
import pytest 
from utils.image_helper import save_screenshot

#14:15
class TestLogin():
    def test_login_valid(self,driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user","secret_sauce")
        save_screenshot(driver, "test_login_valid")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    @pytest.mark.parametrize("username,password", [("abc123","abc123"), ("123","123")])    
    def test_login_invalid(self,driver,username,password):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(username,password)
        save_screenshot(driver, "test_login_invalid")
        assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"