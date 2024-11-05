import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.switch_to.frame("frm2")
driver.find_element(By.ID,"firstName").send_keys("pratik")
time.sleep(5)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,".post-title").text)
time.sleep(3)