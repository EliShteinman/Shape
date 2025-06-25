from math import sqrt
from shape import Shape


class Hexagon(Shape):
    """
    A class representing a hexagon shape.
    """

    def __init__(self, side_length: float) -> None:
        """
        Initialize a Hexagon instance.
        :param side_length:
        """
        if side_length <= 0:
            raise ValueError("Side length must be positive.")
        self.side_length: float = side_length

    def get_area(self) -> float:
        """
        Calculate the area of the hexagon.
        The formula for the area of a regular hexagon is:
        Area = (3 * sqrt(3) * side_length^2) / 2
        """
        return (3 * sqrt(3) / 2) * self.side_length**2

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of the hexagon.
        The formula for the perimeter of a regular hexagon is:
        Perimeter = 6 * side_length
        """
        return 6 * self.side_length

    def __str__(self):
        """
        Return a string representation of the hexagon.
        """
        return f"Hexagon with side length {self.side_length}"

    def __repr__(self):
        """
        Return a detailed string representation of the hexagon.
        """
        return f"Hexagon(side_length={self.side_length})"

    def __eq__(self, other) -> bool:
        """
        Check if two hexagons are equal based on their side lengths.
        """
        if not isinstance(other, Hexagon):
            return NotImplemented
        return self.side_length == other.side_length