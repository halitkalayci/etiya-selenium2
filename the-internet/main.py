# POM mimarisi kullanılmadı.

from main_driver import driver
from time import sleep

# Basic Auth. site domain başlangıcına username:password@ ekleyerek yapılır.
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

sleep(10)
