from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Abstract:
    options = webdriver.ChromeOptions();
    exec_path_chrome = "Drivers/windows/chromedriver.exe"
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)

    # driver = webdriver.Chrome(options=options, executable_path=exec_path_chrome)

