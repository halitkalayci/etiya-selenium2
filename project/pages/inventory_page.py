from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.login_page import LoginPage

class InventoryPage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.inventory_container = (By.ID, "inventory_container")
        self.products = (By.CLASS_NAME, "inventory_item")
        self.product_title = (By.CLASS_NAME, "inventory_item_name")
        self.product_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")
        self.product_img_url = (By.CLASS_NAME, "inventory_item_img")
    
    def load(self,username="standard_user", password="secret_sauce"):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login(username, password)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.wait.until(expected_conditions.visibility_of_element_located(self.inventory_container))
    
    def get_product_list(self):
        container = self.wait.until(expected_conditions.visibility_of_element_located(self.inventory_container))
        products = container.find_elements(*self.products)
        return products
    
    def get_product_title(self,product):
        return product.find_element(*self.product_title).text
    def get_product_price(self,product):
        pass
    def get_product_description(self,product):
        pass
    def get_product_image_url(self,product):
        pass