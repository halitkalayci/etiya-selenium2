from main_driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID, "dropdown")

select = Select(dropdown)

selected_option = select.first_selected_option
print(selected_option.text)

select.select_by_value("1")
sleep(2)

selected_option = select.first_selected_option
print(selected_option.text)

sleep(20)
