import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actual_list=[]
service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
products=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(products)
assert count>0
for product in products:
    actual_list.append(product.find_element(By.XPATH,"h4").text)#grabbing product name
    product.find_element(By.XPATH,"div/button").click()#this is chaining of webelement here findelement will work on each product one by one

time.sleep(5)
assert expected_list==actual_list



#click on cart
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#time.sleep(5)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
prices=driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
total=int(driver.find_element(By.CLASS_NAME,"totAmt").text)
assert total==sum
discounted_price=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discounted_price<total
time.sleep(5)