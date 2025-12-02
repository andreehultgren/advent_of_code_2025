from main import parse_check_ranges


def test_sample_one():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"
    expected_output = 1227775554
    assert parse_check_ranges(input, is_part_two=False) == expected_output


def test_sample_two():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    expected_output = 4174379265
    assert parse_check_ranges(input, is_part_two=True) == expected_output
