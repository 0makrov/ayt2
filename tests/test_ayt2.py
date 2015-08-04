import pytest

import pytest_ayt2


def func(x):
    return x + 1

def test_a():
    assert func(4) == 5
    
def test_b():
	assert 4==4


def test_version():
    assert hasattr(pytest_ayt2, '__version__')
    assert pytest_ayt2.__version__ == '14'
    assert hasattr(pytest_ayt2, 'version')
    assert pytest_ayt2.version == 15