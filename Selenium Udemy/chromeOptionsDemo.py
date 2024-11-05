import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--ignore-certificate-errors")
chrome_option.add_argument("headless")
service_obj=Service()
driver=webdriver.Chrome(service=service_obj,options=chrome_option)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
time.sleep(5)