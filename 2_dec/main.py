from dataclasses import dataclass

from utils import all_items_are_identical, extract_ranges, split_string_into_partitions


@dataclass
class Range:
    from_number: int
    to_number: int

    @staticmethod
    def from_string(range_string: str):
        items = range_string.split("-")
        if len(items) != 2:
            raise ValueError("Range length invalid")
        return Range(int(items[0]), int(items[1]))


def get_list_of_partitions(target: str, max_partition_count=None):
    "Extract a list of partitions (all possible partitions of a string)"
    list_of_partitions = []
    # Check how long the string is
    target_length = len(target)

    # Listen to the max limit. If not set, then we partition
    # up to each individual letter
    range_end = max_partition_count or target_length

    # For each partition count, extract the combinations
    for n_partitions in range(2, range_end + 1):
        # Find all
        partitions = split_string_into_partitions(target, n_partitions)
        if partitions:
            list_of_partitions.append(partitions)
    return list_of_partitions


def is_invalid(number: int, is_part_two=False):
    "Check if an ID (a number) is invalid"
    # Stringify the number:
    target = str(number)

    # Extract each partitioning that can be done
    # for the given string
    list_of_partitions = get_list_of_partitions(
        target,
        max_partition_count=None if is_part_two else 2,
    )

    id_is_invalid = False
    for partitions in list_of_partitions:
        if all_items_are_identical(partitions):
            id_is_invalid = True
    return id_is_invalid


def find_invalid_ids(r: Range, is_part_two: bool):
    "Find all invalid IDs for a given range"
    invalid_ids = []

    # Loop over all the potential numbers
    for test_id in range(r.from_number, r.to_number + 1):
        # Add it if its invalid
        if is_invalid(test_id, is_part_two):
            invalid_ids.append(test_id)

    return invalid_ids


def get_sum_of_invalid_ids(check_range: str, is_part_two: bool):
    "The main solver for the issue. Sum the IDs and return it"
    # Ranges are split by ","
    ranges = [Range.from_string(r) for r in check_range.split(",")]

    aggregated_sum = 0
    for range in ranges:
        invalid_ids = find_invalid_ids(range, is_part_two)
        aggregated_sum += sum(invalid_ids)

    return aggregated_sum


def main(filename: str, is_part_two):
    input_string = extract_ranges(filename)
    results = get_sum_of_invalid_ids(input_string, is_part_two)
    print("Results:", results)


if __name__ == "__main__":
    is_part_two = True
    main("input.txt", is_part_two)
