from math import sqrt
from rectangle import Rectangle


class Triangle(Rectangle):
    """
    A class representing a right-angled triangle, inheriting from Rectangle.
    """

    def __init__(self, base: float, height: float) -> None:
        """
        Initialize a Triangle instance.
        :param base: float - The base of the triangle.
        :param height: float - The height of the triangle.
        """
        super().__init__(base, height)

    def get_area(self) -> float:
        """
        Calculate the area of the triangle.
        A triangle is half the area of the rectangle that surrounds it.
        :return: float - The area of the triangle.
        """
        # Alternative using the Rectangle's area
        # return super().get_area() / 2
        return 0.5 * self.width * self.height

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of a right-angled triangle.
        :return: float - The perimeter of the triangle.
        """
        hypotenuse = sqrt(self.width**2 + self.height**2)
        return self.width + self.height + hypotenuse

    def __str__(self) -> str:
        """
        Return a string representation of the triangle.
        :return: str - String representation of the triangle.
        """
        return f"Triangle with base {self.width} and height {self.height}"
