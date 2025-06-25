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
