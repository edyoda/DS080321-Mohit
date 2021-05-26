## FIXTURES: They are used to have something pre run before
## the actual test.

import pytest

@pytest.fixture
def pre_data():
    data = {'python':3,'django':2,'numpy':1}
    return data

def test_case_1(pre_data):
    assert pre_data['python'] == 3

def test_case_2(pre_data):
    assert pre_data['django'] == 1