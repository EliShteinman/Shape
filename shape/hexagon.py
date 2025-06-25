from math import sqrt
from shape import Shape

class Hexagon(Shape):
    """
    A class representing a hexagon shape.
    """
    def __init__(self, side_length: float) -> None:
        self.side_length: float = side_length

    def get_area(self) -> float:
        """
        Calculate the area of the hexagon.
        The formula for the area of a regular hexagon is:
        Area = (3 * sqrt(3) * side_length^2) / 2
        """
        return (3 * sqrt(3) * self.side_length ** 2) / 2


    def __str__(self):
        """
        Return a string representation of the hexagon.
        """
        return f"Hexagon(side_length={self.side_length})"