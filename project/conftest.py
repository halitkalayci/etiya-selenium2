#Global Ayarlar
import pytest
from selenium.webdriver import Chrome
from utils.image_helper import save_screenshot

@pytest.fixture() #fixture-> Bütün pytest fonksiyonlarına burada tanımlanan bağımlılığı gönderir.
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver # yield-> returnun multiple hali. return->fonks. orada durdurup değeri döndürüyor.
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        driver = item.funcargs.get("driver",None)
        if driver is not None:
            save_screenshot(driver, item.name)

# setup->call->teardown
