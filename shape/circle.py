from math import pi
from shape import Shape


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle instance.
        :param radius:
        """
        self.radius: float = radius

    def get_area(self) -> float:
        """
        Calculate the area of the circle.
        :return: float - The area of the circle.
        """
        return pi * self.radius**2

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.
        :return: float - The perimeter of the circle.
        """
        return 2 * pi * self.radius

    def __str__(self) -> str:
        """
        Return a string representation of the circle.
        :return: str - String representation of the circle.
        """
        return f"Circle with radius {self.radius}"
