import pytest

print 'tttt'

def func(x):
    return x + 1

def test_a():
    assert func(4) == 5
    
def test_b():
    global xxx
	assert xxx==4
