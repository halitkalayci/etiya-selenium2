
def save_screenshot(driver, name="screenshot"):
    import os #operation system
    from datetime import datetime

    #Boilerplate Code
    screenshot_folder = "C:\\Tests\\Screenshots\\" + datetime.now().strftime("%d-%m-%Y")

    os.makedirs(screenshot_folder, exist_ok=True)

    time_stamp = datetime.now().strftime("%H-%M-%S")
    file_name = f"{name}_{time_stamp}_{datetime.now().microsecond}.png"

    file_path = os.path.abspath(os.path.join(screenshot_folder, file_name))
    driver.save_screenshot(file_path)

    return file_path