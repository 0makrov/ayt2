print 'cccc'

def pytest_runtest_setup(item):
    def func(x):
        return x + 1

pytest_plugins = "pytester",