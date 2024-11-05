import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
veg_name=[]
veg_webelm=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
for vegs in veg_webelm:
    veg_name.append(vegs.text)
original_list=veg_name.copy()#make a copy of the list
veg_name.sort()
assert original_list==veg_name

time.sleep(3)