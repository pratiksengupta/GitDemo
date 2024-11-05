#pytest file should start with test_ or ends with _test
#pytest method name should start with test
#to run all test cases in command prompt==> py.test, py.test -v, py.test -v -s
#to run specific test case in command prompt==>py.test filename.py -v -s
#to run different testcases from different file==> py.test -k commonword -v -s (like Creditcard is common in test_demo1 &2)
#in case of regression or smoke test need to mark the method 1st by @pytest.mark.marking_name(here it is smoke). at command prompt we need to type py.test -m marking_name -v -s
#fixture are used as setup or tear down methods for test cases. coftest file is to generalize the fixture to all test cases
import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    print("hello")


def test_SecondgreetCreditcard():
    print("Good Morning")

@pytest.mark.xfail #if we have to run a test case which will be failed we know but don't want to show that in report
def test_prog_not_to_report():
    a=2
    assert a+2==10,"not correct"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
