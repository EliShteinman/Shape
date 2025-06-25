from math import sqrt
from rectangle import Rectangle


class RightAngledTriangle(Rectangle):
    """
    A class representing a right-angled triangle, inheriting from Rectangle.
    """

    def __init__(self, base: float, height: float) -> None:
        """
        Initialize a Triangle instance.
        :param base: float - The base of the triangle.
        :param height: float - The height of the triangle.
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
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

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the triangle.
        :return: str - Detailed string representation of the triangle.
        """
        return f"RightAngledTriangle(base={self.width}, height={self.height})"

    def __eq__(self, other) -> bool:
        """
        Check if two right-angled triangles are equal based on their base and height.
        :param other:
        :return: bool - True if both triangles have the same base and height, False otherwise.
        """
        if not isinstance(other, RightAngledTriangle):
            return NotImplemented
        return (self.width == other.width and self.height == other.height) or (self.width == other.height and self.height == other.width)
