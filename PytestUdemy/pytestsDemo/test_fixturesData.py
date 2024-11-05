import pytest

from PytestUdemy.pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editprofile(self,dataLoad):
        log= self.getlogger()
        log.info(dataLoad[0])
        #print(dataLoad[0])
        #print(dataLoad[1])
        log.info(dataLoad[1])