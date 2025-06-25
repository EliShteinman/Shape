from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass


    @abstractmethod
    def __str__(self) -> str:
        pass
