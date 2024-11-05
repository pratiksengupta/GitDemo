from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
opened_windows=driver.window_handles
driver.switch_to.window(opened_windows[1])
collected_text=(driver.find_element(By.CSS_SELECTOR,".red").text).split(" ")
print(collected_text[4])
driver.switch_to.window(opened_windows[0])
driver.find_element(By.ID,"username").send_keys(collected_text[4])
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.CLASS_NAME,"checkmark").click()
dropdown=Select(driver.find_element(By.XPATH,"//select[@data-style='btn-info']"))
dropdown.select_by_index(0)
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
