from shape import Shape

class Square(Shape):
    def __init__(self, side_length: float) -> None:
        self.side_length:float = side_length

    def get_area(self) -> float:
        return self.side_length ** 2

    def __str__(self) -> str:
        return f"Square with side length {self.side_length}"