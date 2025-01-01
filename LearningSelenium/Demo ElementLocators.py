from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from win32pdhutil import browse
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.nrbcommercialbank.com/home")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#myTopnav > a:nth-child(11)").click()


time.sleep(2)


        # driver.find_element(By.ID, "txtUserName").send_keys('shadman')

#myTopnav > a:nth-child(11)


