import pytest


@pytest.mark.usefixtures("dataload")
class Fixture:
    def test_fixture1(self, dataload):
        print(dataload)

