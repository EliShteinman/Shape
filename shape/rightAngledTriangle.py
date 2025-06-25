from math import sqrt
from shape import Shape


class RightAngledTriangle(Shape):
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
        return 0.5 * self.base * self.height

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of a right-angled triangle.
        :return: float - The perimeter of the triangle.
        """
        hypotenuse = sqrt(self.base**2 + self.height**2)
        return self.base + self.height + hypotenuse

    def __str__(self) -> str:
        """
        Return a string representation of the triangle.
        :return: str - String representation of the triangle.
        """
        return f"Triangle with base {self.base} and height {self.height}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the triangle.
        :return: str - Detailed string representation of the triangle.
        """
        return f"RightAngledTriangle(base={self.base}, height={self.height})"

    def __eq__(self, other) -> bool:
        """
        Check if two right-angled triangles are equal based on their base and height.
        :param other:
        :return: bool - True if both triangles have the same base and height, False otherwise.
        """
        if not isinstance(other, RightAngledTriangle):
            return NotImplemented
        return (self.base == other.base and self.height == other.height) or (
            self.base == other.height and self.height == other.base
        )


