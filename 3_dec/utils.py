import os


def extract_input(filename) -> str:
    "Extract the input from the defined file"
    file_location = os.path.abspath(os.path.join(__file__, os.pardir, filename))
    with open(file_location, "r") as f:
        lines = f.readlines()
    return lines


def to_int_list(input_string: str):
    "Convert a string of integers to a list of integers"
    input_list = list(input_string.replace("\n", ""))
    return [int(x) for x in input_list]


def find_best_option(options: list[int]):
    "Extract the index and value of the first largest number"
    highest_index = 0
    for i, option in enumerate(options):
        if option > options[highest_index]:
            highest_index = i
    return options[highest_index], highest_index


def trim_options_end(full_input: list[int], digits_left: int):
    "Remove the last X digits in a list"
    if digits_left == 1:
        return full_input
    return full_input[: -digits_left + 1]


def convert_it_list_to_int(int_list: list[int]):
    "Convert a list of integers to an integer"
    str_list = [str(x) for x in int_list]
    return int("".join(str_list))


__all__ = [
    "to_int_list",
    "find_best_option",
    "trim_options_end",
    "convert_it_list_to_int",
    "extract_input",
]
