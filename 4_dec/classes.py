# ================ CREATE A NEW DATACLASS ================


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def not_in(self, matrix: "Matrix"):
        return (
            self.x < 0
            or self.y < 0
            or self.x >= matrix.width
            or self.y >= matrix.height
        )

    def in_(self, matrix: "Matrix"):
        return not self.not_in(matrix)

    def __hash__(self):
        return tuple(self.x, self.y)

    def __getitem__(self, key: int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise ValueError("Index out of range")

    def __add__(self, other: "Position"):
        return Position(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x},{self.y})"


class Matrix:
    "A matrix dataclass that is modifyable for convenience"

    def __init__(self, data: list[list[str]], width: int, height: int):
        self.data = data
        self.width = width
        self.height = height

    # Add two built-in funcs to make indexing cleaner

    def __getitem__(self, key: tuple[int, int]) -> str:
        # We index in reverse order to preserve the input map
        return self.data[key[1]][key[0]]

    def __setitem__(self, key: tuple[int, int], value):
        # We index in reverse order to preserve the input map
        self.data[key[1]][key[0]] = value


__all__ = ["Matrix", "Position"]
