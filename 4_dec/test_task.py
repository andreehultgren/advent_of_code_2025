from main import main

sample_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_task_one():
    assert main(sample_input, loop=False) == 13


def test_task_two():
    assert main(sample_input, loop=True) == 43
