from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance.
        :param width: float - The width of the rectangle.
        :param height: float - The height of the rectangle.
        """
        self.width:float = width
        self.height:float = height

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.
        :return: float - The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.
        :return: str - String representation of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height})"