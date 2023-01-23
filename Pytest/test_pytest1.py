import pytest


def test_avi():
    print("hello1")


@pytest.mark.smoke
def test_pytest1():
    print("hello2")


def test_abc():
    print("hello3")


def test_demo2():
    print("hello4")


@pytest.mark.skip
def test_demo1():
    print("hello5")


@pytest.mark.smoke
def test_demo3():
    print("hello6")