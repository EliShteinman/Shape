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

    @abstractmethod
    def __lt__(self, other) -> bool:
        """
        Abstract method to compare two shapes for less than.
        :param other: The other shape to compare with.
        :return: bool - True if this shape is less than the other, False otherwise.
        """
        pass
