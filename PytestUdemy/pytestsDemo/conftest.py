import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be execute first")
    yield
    print("I'll execute last")


@pytest.fixture()
def dataLoad():
    print("user data is being created")
    return ["pratik","sengupta","p.sen.80@gmail.com"]

@pytest.fixture(params=[("chrome","pratik","sengupta"),("Firefox","p.sen.80@gmail.comD:\Python Udemy\PytestUdemy\pytestsDemo"),"IE"])
def crossBrowser(request):
    return request.param