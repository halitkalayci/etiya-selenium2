# 1- Built-in -> python'ın içine gömülü gelen modüller
import math # built-in
# 2- Kendi yazdığımız moduller
from calculator import calculate_tax # file-based modules
# third-party
#import requests # tüm requests paketini bu dosyaya import et.
from requests import get as http_get

print(math.sqrt(64))
print(calculate_tax(100))

response = http_get("https://google.com")
print(response.status_code)