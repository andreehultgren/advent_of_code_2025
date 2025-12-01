from dataclasses import dataclass
from typing import Literal
import os


# Create dataclasses for easier workflows
@dataclass
class Rotation:
    "One single rotation of the safe"

    direction: Literal["left", "right"]
    number: int


@dataclass
class Position:
    "One position and the aggregated counts that we want to track"

    number: int
    total_zero_passes: int = 0
    total_zero_stops: int = 0


def _extract_rotations_strings(filename):
    "Utility function to extract rotations"
    file_location = os.path.abspath(os.path.join(__file__, os.pardir, filename))
    with open(file_location, "r") as f:
        rotation_strings = f.readlines()
    return rotation_strings


def _parse_rotation(rotation_string):
    direction_char = rotation_string[0]
    length = int(rotation_string[1:])

    return Rotation(
        direction="left" if direction_char == "L" else "right", number=length
    )


def get_next_position(position: Position, rotation: Rotation, n_steps: int):
    "Combine a position and a rotation to get the next position"

    # =========== COMPUTE ROTATION ==============
    if rotation.direction == "right":
        new_location = position.number + rotation.number
    else:
        new_location = position.number - rotation.number

    # Extract the new value after a rotation
    moduled_location = new_location % 100

    # Extract how many times we pass the zero value
    passes_zero_times = round(abs((new_location - moduled_location) / n_steps))

    # =========== EDGE CASES ==============
    if rotation.direction == "left":
        # If we rotate to the left, starting from 0
        # (then we have already passed 0 in the previous rotation and counted it)
        if position.number == 0:
            passes_zero_times -= 1
        # If we rotate to the left and stop at 0, then we count that rotation
        if moduled_location == 0:
            passes_zero_times += 1
    # Q: Don't the two actions cancel eachother out?
    # A: If we rotate left twice in a row and stop at 0, then yes.
    # but if we rotate right to 0 and then back, then it matters.

    # =========== UPDATE AGGREGATION ==============
    new_zero_passes = position.total_zero_passes + passes_zero_times
    new_zero_stops = position.total_zero_stops
    if moduled_location == 0:
        new_zero_stops += 1

    # Return the new position
    return Position(
        number=moduled_location,
        total_zero_passes=new_zero_passes,
        total_zero_stops=new_zero_stops,
    )


def main(start_position, n_steps, filename):
    # Start at the starting position
    position = Position(start_position)

    # Extract the rotations from the input file
    rotation_strings = _extract_rotations_strings(filename)
    rotations = map(_parse_rotation, rotation_strings)

    # Follow the rotations and track the values via the dataclass
    for rotation in rotations:
        position = get_next_position(position, rotation, n_steps)

    # Print the results
    print("The password is:", position.total_zero_stops)
    print("Total zero passes", position.total_zero_passes)


if __name__ == "__main__":
    # Define the parameters for the problem
    input_filename = "input.txt"
    sample_filename = "sample.txt"
    main(start_position=50, n_steps=100, filename=input_filename)
