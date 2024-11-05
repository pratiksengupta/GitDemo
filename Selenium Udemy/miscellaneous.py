import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#to run as headless mode. means chrome will not be invoked but at backend it will work
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")#to handle certificate errors

service_obj=Service()
driver=webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")#to scroll to bottom
time.sleep(3)
driver.execute_script("window.scrollBy(0,500);")#to scroll to certain position
time.sleep(3)
driver.get_screenshot_as_file("screen1.png")
