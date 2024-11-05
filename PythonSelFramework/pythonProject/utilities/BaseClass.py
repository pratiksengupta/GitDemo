import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggername= inspect.stack()[1][3]
        logger=logging.getLogger(loggername)#(__name__)is for capturing the file name



        filehandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOPtionByText(self,locator,index_no):
        dropdown = Select(locator)
        # dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(index_no)
