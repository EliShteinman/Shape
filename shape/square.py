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
