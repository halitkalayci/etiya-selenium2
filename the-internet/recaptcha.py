from main_driver import driver
from time import sleep
from selenium.webdriver.common.by import By

driver.get("https://patrickhlauke.github.io/recaptcha/")

iframe_captcha = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/iframe")

driver.switch_to.frame(iframe_captcha)

click_span = driver.find_element(By.ID, "recaptcha-anchor")
click_span.click()

sleep(1000)