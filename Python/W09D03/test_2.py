## Way of Selecting or filtering test cases:
# 1) Running the test cases with substring matching approach

def func(x):
    if x%2==0:
        return x+5
    else:
        return x-5

def test_case_by_Mohit():
    assert func(3) == 8

def test_case_by_Vishal():
    assert func(2) == 7

def test_case_by_Mohit2():
    assert 2 == 2

# we pass substring to match with "-k" flag
# cmd: py.test -k test_case_by_Mohit