from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver
    countryfield=(By.ID,"country")
    country=(By.LINK_TEXT,"India")
    checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit=(By.XPATH,"//input[@type='submit']")
    success_message=(By.CSS_SELECTOR,".alert-success")
    def countryField(self):
        return self.driver.find_element(*ConfirmPage.countryfield)
    def getcountry(self):
        return self.driver.find_element(*ConfirmPage.country)
    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    def getsubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)
    def getsuccess_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)

