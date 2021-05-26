## Way of Selecting or filtering test cases:
## 2) Marking the test cases

import pytest

def func(x):
    if x%2==0:
        return x+5
    else:
        return x-5

@pytest.mark.bygirl
def test_case_by_Kanishka():
    assert func(3) == 8

@pytest.mark.bygirl
def test_case_by_Revathi():
    assert func(2) == 7

@pytest.mark.byboy
def test_case_by_Atul():
    assert 2 == 2

## -m is used to tell pytest that we are going to pass the name
## of the marker.
## cmd: py.test -m bygirl