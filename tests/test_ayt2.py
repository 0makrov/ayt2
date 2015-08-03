import pytest


def func(x):
    return x + 1

def test_a():
    assert func(4) == 5
    print 'tttt'
    
def test_b():
	assert 4==4
