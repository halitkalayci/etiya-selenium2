from pages.inventory_page import InventoryPage
from utils.data_helper import read_csv_data
class TestInventory():
    def test_product_length(self,driver):
        inv_page = InventoryPage(driver)
        inv_page.load()
        products = inv_page.get_product_list()
        assert len(products) == 6
    def test_product_information(self,driver):
        csv_data = read_csv_data(r"C:\Users\PC1\Desktop\Projects\Education\Python\etiya-selenium2\project\data\products.csv")
        inv_page = InventoryPage(driver)
        inv_page.load()
        products = inv_page.get_product_list()
        for index, product in enumerate(products):
            csv_item = csv_data[index]
            title = inv_page.get_product_title(product)
            description = inv_page.get_product_description(product)
            price = inv_page.get_product_price(product)
            img_url = inv_page.get_product_image_url(product)
            assert csv_item[0] == title
            assert csv_item[1] == description
            assert csv_item[2] == price
            assert csv_item[3] == img_url