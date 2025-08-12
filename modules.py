# 1- Built-in -> python'ın içine gömülü gelen modüller
import math # built-in
# 2- Kendi yazdığımız moduller
import calculator # file-based modules
# third-party
import requests

print(math.sqrt(64))
print(calculator.calculate_tax(100))

response = requests.get("https://google.com")
print(response.status_code)