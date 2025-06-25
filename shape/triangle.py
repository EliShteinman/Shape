from rectangle import Rectangle

class Triangle(Rectangle):
    """
    A class representing a triangle, inheriting from Rectangle.
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
        :return: float - The area of the triangle.
        """
        # retutn super().get_area() / 2
        return 0.5 * self.width * self.height

    def __str__(self) -> str:
        """
        Return a string representation of the triangle.
        :return: str - String representation of the triangle.
        """
        return f"Triangle with base {self.width} and height {self.height}"