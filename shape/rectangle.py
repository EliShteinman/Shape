from .shape import Shape


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape class.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance.
        :param width: float - The width of the rectangle.
        :param height: float - The height of the rectangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width: float = width
        self.height: float = height

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.
        :return: float - The area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        :return: float - The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.
        :return: str - String representation of the rectangle.
        """
        return f"Rectangle with width {self.width} and height {self.height}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the rectangle.
        :return: str - Detailed string representation of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other) -> bool:
        """
        Check if two rectangles are equal based on their width and height.
        :param other:
        :return: bool - True if both rectangles have the same width and height, False otherwise.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented
        return (self.width == other.width and self.height == other.height) or (
            self.width == other.height and self.height == other.width
        )

    def __mul__(self, scalar: float) -> "Rectangle":
        """
        Scale the rectangle by a scalar value.
        :param scalar: float - The scalar value to scale the rectangle.
        :return: Rectangle - A new Rectangle instance with scaled dimensions.
        """
        if scalar <= 0:
            raise ValueError("Scalar must be positive.")
        return Rectangle(self.width * scalar, self.height * scalar)
