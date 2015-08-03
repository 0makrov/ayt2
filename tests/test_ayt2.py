import pytest

print 'tttt'

def func(x):
    return x + 1

def test_a():
    assert func(4) == 6
    
def test_b():
	assert 1==1
