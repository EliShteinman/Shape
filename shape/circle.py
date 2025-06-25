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
        if radius <= 0:
            raise ValueError("Radius must be positive.")
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
        return f"A circle with a radius of {self.radius}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the circle.
        :return: str - Detailed string representation of the circle.
        """
        return f"Circle(radius={self.radius})"

    def __eq__(self, other) -> bool:
        """
        Check if two circles are equal based on their radii.
        :param other: Circle - The other circle to compare with.
        :return: bool - True if both circles have the same radius, False otherwise.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius


