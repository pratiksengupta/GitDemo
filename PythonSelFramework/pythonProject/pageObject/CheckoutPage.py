from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
    products=(By.CSS_SELECTOR, ".card")
    #producttext=(By.CSS_SELECTOR, "h4")
    checkoutbtn1=(By.CSS_SELECTOR,".btn-primary")
    checkoutbtn2=(By.CSS_SELECTOR,".btn-success")
    def getproducts(self):
        return self.driver.find_elements(*CheckoutPage.products)
    # def getproducttext(self):
    #     return self.driver.find_element(*CheckoutPage.producttext)
    def getcheckoutbtn1(self):
        return self.driver.find_element(*CheckoutPage.checkoutbtn1)
    def getcheckoutbtn2(self):
        self.driver.find_element(*CheckoutPage.checkoutbtn2).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage


