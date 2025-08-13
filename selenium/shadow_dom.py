from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = Chrome()
driver.get("https://the-internet.herokuapp.com/shadowdom")

heading = driver.find_element(By.XPATH, "//*[@id='content']/h1")
print(heading.text)

span = driver.find_element(By.XPATH, "//*[@id='content']/my-paragraph[1]/span")
print(span.text)


my_paragprah = driver.find_element(By.TAG_NAME, "my-paragraph")
print(my_paragprah.text)
#my_paragprah.shadow_root.find_element()
#p = my_paragprah.shadow_root.find_element(By.TAG_NAME, "p")
#print(p.text)