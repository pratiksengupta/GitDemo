import pytest


@pytest.mark.smoke
@pytest.mark.skip #this is to skip any testcase
def test_firstprogram():
    msg="hello"
    assert msg=="hi","test failed due to mismatch of string"

def test_SecondCreditcard():
    a=4
    b=6
    assert a+2==6, "addition does not match"

