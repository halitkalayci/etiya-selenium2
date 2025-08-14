from pages.inventory_page import InventoryPage
from time import sleep
class TestInventory():
    def test_product_length(self,driver):
        inv_page = InventoryPage(driver)
        inv_page.load()
        sleep(10)