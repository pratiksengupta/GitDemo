import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #cssselector= tagname[attribute='value'] or #id or .classname
    driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("pratik")
    driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
    driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID,"exampleCheck1").click()
    #handle static dropdown
    dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
    #dropdown.select_by_visible_text("Female")
    dropdown.select_by_index(1)
    driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
    #xpath=//tagname[@attribute='value']
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("test")
    #driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

    message=driver.find_element(By.CLASS_NAME,"alert-success").text
    print(message)
    assert "Success" in message
    time.sleep(2)
except Exception as e:
    print(e)