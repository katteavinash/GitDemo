import pytest


@pytest.fixture()
def dataload():
    print("welcome to fixture")
    return ["avinash", "katte", "tester"]



