import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:#we assuming here position of radio button will change
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radio_buttons=driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
radio_buttons[1].click()#we assuming here position of radio button will not change
assert radio_buttons[1].is_selected()
# for button in radio_buttons:
#     if button.get_attribute("value")=="radio2":
#         button.click()
#         assert button.is_selected()
#         break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(5)