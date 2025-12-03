from utils import (
    convert_it_list_to_int,
    extract_input,
    find_best_option,
    to_int_list,
    trim_options_end,
)


def main(input_string, n_digits_to_select=2):
    # Parse the input
    input_integers = to_int_list(input_string)

    # Define the starting position of the loop
    digits_left = n_digits_to_select
    remaining_options = input_integers
    selected_numbers = []

    while digits_left:
        # Remove the final X digits so we do not select a number
        # such that we cannot finish the digit count
        options = trim_options_end(remaining_options, digits_left)

        # Find and select the best option given the remaining options
        largest_digit, largest_index = find_best_option(options)
        selected_numbers.append(largest_digit)

        # Remove everything before and including the selected option
        remaining_options = remaining_options[largest_index + 1 :]

        # Restart the loop
        digits_left -= 1

    return convert_it_list_to_int(selected_numbers)


if __name__ == "__main__":
    input_lines = extract_input("input.txt")

    print("========= TASK 1 =========")
    total_joltage_task_1 = 0
    for line in input_lines:
        total_joltage_task_1 += main(line)
    print("Results: ", total_joltage_task_1)

    print("========= TASK 2 =========")
    total_joltage_task_2 = 0
    for line in input_lines:
        total_joltage_task_2 += main(line, n_digits_to_select=12)
    print("Results: ", total_joltage_task_2)
