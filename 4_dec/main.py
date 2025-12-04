import os

from classes import Matrix, Position

# =================== DEFINE CONSTANTS ===================
TOILET_ROLL = "@"
NO_TOILET_ROLL = "."
REMOVED_TOILET_ROLL = "x"
MAX_NEARBY_PAPSERS = 4


# =============== DEFINE UTILITY FUNCTIONS ===============


def _convert_string_to_matrix(input_string: str):
    "Clean up incoming string and output a matrix"
    # Split the input at the breaklines (rows)
    split_input = input_string.split("\n")

    # Remove extra padding that might appear
    stripped_rows = [r.strip() for r in split_input]

    # Remove empty rows from the data
    input_rows = [r for r in stripped_rows if r != ""]

    # Turn it into a list of lists and create Matrix
    data = [list(row) for row in input_rows]
    height = len(data)
    width = len(data[0])
    return Matrix(data, width, height)


def _get_positions_from_matrix(matrix: Matrix) -> list[Position]:
    "Extract all possible locations inside the matrix"
    positions = []
    # We could use combinations, but my ambition is to
    # not rely on external packages
    for x in range(matrix.width):
        for y in range(matrix.height):
            positions += [Position(x, y)]
    return positions


def _get_input(filename):
    "Extract the string from a file"
    # Getting the input.txt relative to the file
    # makes it independent of caller directory
    path = os.path.join(__file__, os.pardir, filename)
    with open(os.path.abspath(path)) as f:
        content = f.read()
    return content


def _count_neighours(matrix: Matrix, pos: Position, character=TOILET_ROLL):
    n_neighbours = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if not (dx or dy):
                continue
            target_position = pos + Position(dx, dy)
            if target_position.not_in(matrix):
                continue
            if matrix[target_position] == character:
                n_neighbours += 1
    return n_neighbours


# ==================== THE MAIN LOGIC ====================


def main(input_string, loop=False):
    matrix = _convert_string_to_matrix(input_string)
    total_removed_rolls = 0

    while True:
        removed_paper_rolls = []
        positions = _get_positions_from_matrix(matrix)
        for pos in positions:
            if matrix[pos] != TOILET_ROLL:
                continue
            n_neighbours = _count_neighours(matrix, pos, TOILET_ROLL)
            if n_neighbours < MAX_NEARBY_PAPSERS:
                removed_paper_rolls.append(pos)

        for pos in removed_paper_rolls:
            matrix[pos] = NO_TOILET_ROLL

        total_removed_rolls += len(removed_paper_rolls)
        if not removed_paper_rolls or not loop:
            return total_removed_rolls


if __name__ == "__main__":
    task_input = _get_input("input.txt")
    print("===== Task 1 =====")
    print(main(task_input, loop=False))

    print("===== Task 2 =====")
    print(main(task_input, loop=True))

__all__ = ["main"]
