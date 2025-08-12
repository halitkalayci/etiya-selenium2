from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time

options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")

driver = Chrome(options=options)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(3) # Amatör çözüm.
# Beklemek.
username_input = driver.find_element(By.ID, 'user-name') #
username_input.send_keys("standard_user") #

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()

time.sleep(500)


#login_failure_invalid_password – Yanlış şifre ile giriş yapılamadığını doğrula
#add_product_to_cart – Ürün sepete eklendiğinde sepet ikonundaki sayının arttığını kontrol et