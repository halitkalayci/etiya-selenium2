from main_driver import driver
from selenium.webdriver.common.by import By
from time import sleep

driver.get("https://the-internet.herokuapp.com/windows")

click_here = driver.find_element(By.XPATH, "//*[@id='content']/div/a")
click_here.click()

# Eğer tarayıcıda birden fazla sekme açıksa hangisine focus olduğum görüntüyle değil kodla çözülmeli.
windows = driver.window_handles
driver.switch_to.window(windows[1])

h3 = driver.find_element(By.XPATH, "/html/body/div/h3")
print(h3.text)
sleep(10)