def pytest_addoption(parser):
    print('rrrr') #nothing doing

    
def tear_down():
    print "\nTEARDOWN after all tests"
    
@pytest.fixture(scope="session", autouse=True)
def set_up(request):
    print "\nSETUP before all tests"