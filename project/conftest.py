#Global Ayarlar
import pytest
from selenium.webdriver import Chrome


@pytest.fixture() #fixture-> Bütün pytest fonksiyonlarına burada tanımlanan bağımlılığı gönderir.
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver # yield-> returnun multiple hali. return->fonks. orada durdurup değeri döndürüyor.
    driver.quit()