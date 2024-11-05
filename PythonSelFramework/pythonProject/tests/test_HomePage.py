import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):

        log=self.getlogger()


        homepage=HomePage(self.driver)

        # cssselector= tagname[attribute='value'] or #id or .classname
        log.info("First name is"+getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(getData["password"])
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        homepage.getcheckbox().click()

        # handle static dropdown
        self.selectOPtionByText(homepage.getStatic_dropdown(), getData["gender"])
        
        homepage.getRadio_button().click()

        # xpath=//tagname[@attribute='value']
        homepage.getsubmit().click()
        homepage.get_ip_box_text().send_keys(getData["text"])

        # driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

        message=homepage.get_success_msg().text

        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getData("Testcase1"))
    def getData(self,request):
        return request.param
