import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
product_name=[]
want_to_buy="Nokia Edge"
products=driver.find_elements(By.CSS_SELECTOR,".card")
#time.sleep(10)
for product in products:
    if (want_to_buy==product.find_element(By.CSS_SELECTOR,"h4").text):
        product.find_element(By.CSS_SELECTOR,".card button").click()

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
assert driver.find_element(By.ID,"country").get_attribute("value")=="India"
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
success_msg=driver.find_element(By.CSS_SELECTOR,".alert-success").text
assert "Success" in success_msg
    


time.sleep(5)