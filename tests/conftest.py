import pytest


def tear_down():
    print "\nTEARDOWN after all tests"
    
@pytest.fixture(scope="session", autouse=True)
def set_up(request):
    print "\nSETUP before all tests"

def pytest_runtest_setup(item):
    print ("setting up", item)

pytest_plugins = "pytester",