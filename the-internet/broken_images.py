from main_driver import driver
from selenium.webdriver.common.by import By
import requests

driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME, "img")

for image in images:
    image_link = image.get_attribute("src")
    response = requests.get(image_link)
    if response.status_code != 200:
        print(f"Bozuk image: {image_link}")