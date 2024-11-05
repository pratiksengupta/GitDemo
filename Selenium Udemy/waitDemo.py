import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
products=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(products)
assert count>0
for product in products:
    product.find_element(By.XPATH,"div/button").click()#this is chaining of webelement here findelement will work on each product one by one

#time.sleep(5)
#click on cart
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
#time.sleep(5)