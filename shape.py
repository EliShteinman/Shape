from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all shapes.
    """

    @abstractmethod
    def get_area(self) -> float:
        """
        Abstract method to calculate the area of the shape.
        :return: float - The area of the shape.
        """
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        """
        Abstract method to calculate the perimeter of the shape.
        :return: float - The perimeter of the shape.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method to return a string representation of the shape.
        :return: str - String representation of the shape.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method to return a detailed string representation of the shape.
        :return: str - Detailed string representation of the shape.
        """
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        """
        Abstract method to compare two shapes for equality.
        :param other: The other shape to compare with.
        :return: bool - True if the shapes are equal, False otherwise.
        """
        pass

    def __lt__(self, other) -> bool:
        """
        Compares this shape to another based on their area.
        :param other: An object that has a get_area() method.
        :return: bool - True if this shape's area is less than the other's, False otherwise.
        """
        if not isinstance(other, Shape):
            return NotImplemented
        return self.get_area() < other.get_area()
