import os


def extract_ranges(filename) -> str:
    "Utility function to extract rotations"
    file_location = os.path.abspath(os.path.join(__file__, os.pardir, filename))
    with open(file_location, "r") as f:
        check_ranges = f.read()
    return check_ranges


def split_string_into_partitions(target: str, n_partitions: int):
    if (len(target) % n_partitions) != 0:
        return []

    partition_length = len(target) // n_partitions

    # Create the partitions
    partitions = []
    for i in range(n_partitions):
        start = i * partition_length
        end = (i + 1) * partition_length
        partitions.append(target[start:end])
    return partitions


def all_items_are_identical(list_of_values):
    if len(list_of_values) == 1:
        return True

    all_are_identical = True
    for value in list_of_values:
        if value != list_of_values[0]:
            all_are_identical = False
            break

    return all_are_identical


__all__ = [
    "extract_ranges",
    "split_string_into_partitions",
    "all_items_are_identical",
]
