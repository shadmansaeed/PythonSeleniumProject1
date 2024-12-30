from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from win32pdhutil import browse
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.nrbcommercialbank.com/home")

time.sleep(3)
driver.maximize_window()
time.sleep(3)
print(driver.title)
driver.close()



