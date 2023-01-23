import pytest


@pytest.mark.smoke
def test_pytest():
    print("hello")


def test_avi3():
    print("hi1")


def test_pytest2():
    print("hi2")


@pytest.mark.smoke
def test_abc3():
    print("hi3")
