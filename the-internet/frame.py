from main_driver import driver
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, "mce_0_ifr")

driver.switch_to.frame(iframe)

p = driver.find_element(By.XPATH,"//*[@id='tinymce']/p")

print(p.text)
