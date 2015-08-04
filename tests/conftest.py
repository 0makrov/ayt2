import pytest




def pytest_runtest_setup(item):
    print ("setting up", item)

pytest_plugins = "pytester",