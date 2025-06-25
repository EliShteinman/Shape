from rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, side_length: float) -> None:
        """
        Initialize a Square instance.
        :param side_length: float - The length of the sides of the square.
        """
        if side_length <= 0:
            raise ValueError("Side length must be positive.")
        super().__init__(side_length, side_length)

    def get_area(self) -> float:
        """
        Calculate the area of the square.
        :return: float - The area of the square.
        """
        return super().get_area()

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of the square.
        :return: float - The perimeter of the square.
        """
        return super().get_perimeter()

    def __str__(self) -> str:
        """
        Return a string representation of the square.
        :return: str - String representation of the square.
        """
        return f"Square with side length {self.width}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the square.
        :return: str - Detailed string representation of the square.
        """
        return f"Square(side_length={self.width})"

    def __eq__(self, other) -> bool:
        """
        Check if two squares are equal based on their side lengths.
        :param other:
        :return: bool - True if both squares have the same side length, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.width == other.width

    def __mul__(self, scalar: float) -> "Square":
        """
        Scale the square by a scalar value.
        :param scalar: float - The scalar value to scale the square.
        :return: Square - A new Square instance scaled by the scalar value.
        """
        if scalar <= 0:
            raise ValueError("Scalar must be positive.")
        return Square(self.width * scalar)
