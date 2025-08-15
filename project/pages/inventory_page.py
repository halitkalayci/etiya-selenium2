from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
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
        self.product_img_url = (By.TAG_NAME, "img")
        self.sort_select_container = (By.CSS_SELECTOR, ".select_container")
        self.cart_badge = (By.CSS_SELECTOR, "[data-test=\"shopping-cart-badge\"]")
    
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
        return product.find_element(*self.product_price).text
    def get_product_description(self,product):
        return product.find_element(*self.product_desc).text
    def get_product_image_url(self,product):
        img = product.find_element(*self.product_img_url)
        return img.get_attribute("src")

    def is_sort_dropdown_visible(self):
        try:
            el = self.wait.until(expected_conditions.visibility_of_element_located(self.sort_select_container))
            return el.is_displayed()
        except TimeoutException:
            return False

    def add_to_cart(self, product_test_id):
        selector = (By.CSS_SELECTOR, f"[data-test=\"add-to-cart-{product_test_id}\"]")
        self.wait.until(expected_conditions.element_to_be_clickable(selector)).click()

    def wait_cart_badge_text(self, expected_text):
        try:
            return self.wait.until(expected_conditions.text_to_be_present_in_element(self.cart_badge, expected_text))
        except TimeoutException:
            return False

    def get_cart_badge_text(self):
        try:
            badge = self.wait.until(expected_conditions.visibility_of_element_located(self.cart_badge))
            return badge.text
        except TimeoutException:
            return ""