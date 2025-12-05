from main import compute_range, main

sample_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


sample_input_2 = """
1-4
4-6
4-10
8-10
11-17
12-12
13-15
25-30

1
5
8
11
17
32
"""


def test_task_one():
    assert main(sample_input) == 3


def test_task_two():
    assert compute_range(sample_input) == 14


def test_task_three():
    assert compute_range(sample_input_2) == 23
