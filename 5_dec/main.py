import os

# =============== DEFINE UTILITY FUNCTIONS ===============


def _convert_input_to_fresh_and_available(input_string: str):
    "Clean up incoming string and output a matrix"
    # Split the input at the breaklines (rows)
    split_input = input_string.split("\n")

    # Remove extra padding that might appear
    stripped_rows = [r.strip() for r in split_input]

    if stripped_rows[0] == "":
        stripped_rows.pop(0)
    if stripped_rows[-1] == "":
        stripped_rows.pop(-1)

    # We now have a clean dataset. Split into two sets:
    for i, row in enumerate(stripped_rows):
        if row == "":
            break

    return stripped_rows[:i], stripped_rows[i + 1 :]


def _get_input(filename):
    "Extract the string from a file"
    # Getting the input.txt relative to the file
    # makes it independent of caller directory
    path = os.path.join(__file__, os.pardir, filename)
    with open(os.path.abspath(path)) as f:
        content = f.read()
    return content


# ==================== THE MAIN LOGIC ====================


def main(input_string):
    # Extract the fresh and available lists
    fresh, available = _convert_input_to_fresh_and_available(input_string)

    # Add all available IDs to a set
    total_available = set()
    for value_str in available:
        total_available.add(int(value_str))

    # Don't to set comparison, because RAM won't be sufficient.
    fresh_and_available = set()
    for fresh_range in tqdm(fresh):
        # Instead, loop over the range and add all matching available items
        start_str, end_str = fresh_range.split("-")
        start = int(start_str)
        end = int(end_str)
        for a in total_available:
            if start <= a and a <= end:
                fresh_and_available.add(a)

    # This will give us the join anyways :)
    return len(fresh_and_available)


def compute_range(input_string):
    fresh, _ = _convert_input_to_fresh_and_available(input_string)
    # Get the ranges
    ranges = []
    total_POIs = set()

    # We loop over each range that we have as input
    for f in fresh:
        start_str, end_str = f.split("-")
        start = int(start_str)
        end = int(end_str)

        # We mark each step into a set (for the loop later)
        total_POIs.add(start)
        total_POIs.add(end)

        # And we add the range into a list (for checking inclusions later)
        if start <= end:
            ranges.append([start, end])
        else:
            ranges.append([end, start])

    # Sort all the indexes that we added.
    # Now we have a list of all "points of interest"
    # Then we just have to check if the ranges between each
    # point of interest is inclusive or exclusive.
    all_POIs = sorted(list(total_POIs))

    def is_in_range(value):
        for start, end in ranges:
            if (value >= start and value <= end) or (value <= start and value >= end):
                return True
        return False

    total_sum = 0
    last_span_was_gap = True

    # Let's start looping over the points of interests
    for i, current_id in enumerate(all_POIs):
        # The last point of interest is ignored
        # (since the number has already been accounted for)
        if len(all_POIs) - 1 == i:
            continue

        # Get the next POI and compute the range
        next_id = all_POIs[i + 1]
        n_items = next_id - current_id

        if n_items == 1:
            # If it is just a 1-off, then both are
            # included by definition and we
            # can just move one step
            total_sum += 1
            continue

        # We have now 2 or more values between the
        # two POIs, so we can have "excluded" options

        # Check if the next ID is included in the ranges
        # if it is, then all IDs between the two POIs
        # are included
        if is_in_range(current_id + 1):
            total_sum += n_items
            if last_span_was_gap:
                total_sum += 1
            last_span_was_gap = False
            continue

        # We have a range of non-included IDs.
        # proceed to the next POI.
        last_span_was_gap = True

    return total_sum


if __name__ == "__main__":
    task_input = _get_input("input.txt")
    print("===== Task 1 =====")
    print(main(task_input))

    print("===== Task 2 =====")
    print(compute_range(task_input))

__all__ = ["main"]
