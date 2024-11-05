from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    shop=(By.LINK_TEXT, "Shop")
    name=(By.CSS_SELECTOR,"input[name='name']")
    email=(By.NAME,"email")
    password=(By.ID,"exampleInputPassword1")
    checkbox=(By.ID,"exampleCheck1")
    static_dropdown=(By.ID,"exampleFormControlSelect1")
    radio_button=(By.CSS_SELECTOR,"#inlineRadio1")
    submit=(By.XPATH,"//input[@type='submit']")
    ip_text_box=(By.XPATH,"(//input[@type='text'])[3]")
    success_msg=(By.CLASS_NAME,"alert-success")
    def getname(self):
        return self.driver.find_element(*HomePage.name)
    def getemail(self):
        return self.driver.find_element(*HomePage.email)
    def getpassword(self):
        return self.driver.find_element(*HomePage.password)
    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getStatic_dropdown(self):
        return self.driver.find_element(*HomePage.static_dropdown)
    def getRadio_button(self):
        return self.driver.find_element(*HomePage.radio_button)
    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def get_ip_box_text(self):
        return self.driver.find_element(*HomePage.ip_text_box)
    def get_success_msg(self):
        return self.driver.find_element(*HomePage.success_msg)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page=CheckoutPage(self.driver)
        return checkout_page


