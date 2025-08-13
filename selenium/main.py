from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")

driver = Chrome(options=options)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Username inputu gözükene kadar maksimum 10 saniye bekle.
wait = WebDriverWait(driver,timeout=10,poll_frequency=0.5)
username_input = wait.until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
username_input.send_keys("standard_user") #
# presence_of_element_located -> Element DOM ağacında var mı?
# visibility_of_element_located -> Element DOM ağacında var mı ve görünür mü?
# element_to_be_clickable -> Element DOM ağacında var mı, görünür mü ve tıklanabilir mi?
# text_to_be_present_in_element -> Elementin içinde spesifik bir yazı görünene kadar.
# alert_is_present -> Tarayıcı bir alert çıkarana kadar bekler.
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
# Yeni bir işlem varsa bekle.
time.sleep(500)

#login_failure_invalid_password – Yanlış şifre ile giriş yapılamadığını doğrula
#add_product_to_cart – Ürün sepete eklendiğinde sepet ikonundaki sayının arttığını kontrol et