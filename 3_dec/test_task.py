import pytest
from main import main

test_cases_task_one = [
    ("987654321111111", 98),
    ("811111111111119", 89),
    ("234234234234278", 78),
    ("818181911112111", 92),
]
test_cases_task_two = [
    ("987654321111111", 987654321111),
    ("811111111111119", 811111111119),
    ("234234234234278", 434234234278),
    ("818181911112111", 888911112111),
]


@pytest.mark.parametrize("test_case", test_cases_task_one)
def test_sample_one(test_case):
    assert main(test_case[0]) == test_case[1]


@pytest.mark.parametrize("test_case", test_cases_task_two)
def test_sample_two(test_case):
    assert main(test_case[0], 12) == test_case[1]
