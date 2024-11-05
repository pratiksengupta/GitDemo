from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
opened_windows=driver.window_handles
driver.switch_to.window(opened_windows[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(opened_windows[0])
assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text

