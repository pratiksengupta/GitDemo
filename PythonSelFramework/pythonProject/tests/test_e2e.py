import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

#from pageObject.CheckoutPage import CheckoutPage
#from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getlogger()
        homepage=HomePage(self.driver)
        checkout_page=homepage.shopItems()
        log.info("Getting all the card titles")
        product_name = []
        want_to_buy = "Nokia Edge"

        products=checkout_page.getproducts()

        # time.sleep(10)
        for product in products:
            if want_to_buy == product.find_element(By.CSS_SELECTOR, "h4").text:
                product.find_element(By.CSS_SELECTOR, ".card button").click()

        checkout_page.getcheckoutbtn1().click()
        confirmpage=checkout_page.getcheckoutbtn2()



        log.info("Entering country name as Ind")
        confirmpage.countryField().send_keys("Ind")



        self.verifyLinkPresence("India")
        
        confirmpage.getcountry().click()

        assert self.driver.find_element(By.ID, "country").get_attribute("value") == "India"
        confirmpage.getcheckbox().click()

        confirmpage.getsubmit().click()

        success_msg=confirmpage.getsuccess_message().text
        log.info("Text received fro application is "+success_msg)

        assert "Success" in success_msg

        time.sleep(5)




