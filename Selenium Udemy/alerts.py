import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name="Pratik"
service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Your Name']").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alertText=alert.text
print(alertText)
assert name in alertText
alert.accept()

driver.find_element(By.ID,"confirmbtn").click()
confirm=driver.switch_to.alert
time.sleep(3)
confirm.dismiss()
time.sleep(5)