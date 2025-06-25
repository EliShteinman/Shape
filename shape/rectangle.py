from shape import Shape


class Rectangle(Shape):
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
