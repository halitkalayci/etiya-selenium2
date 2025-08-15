from main_driver import driver
from selenium.webdriver.common.by import By
from time import sleep

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

js_alert = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")

js_alert.click()
sleep(1)
alert = driver.switch_to.alert
alert.accept()
sleep(5)

js_confirm = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
js_confirm.click()
sleep(1)
alert2 = driver.switch_to.alert
alert2.accept() #onay - dismiss->reddet.
sleep(5)

js_prompt = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
js_prompt.click()
sleep(1)
alert3 = driver.switch_to.alert
alert3.send_keys("Merhaba")
alert3.accept()
sleep(3)

# 11:05