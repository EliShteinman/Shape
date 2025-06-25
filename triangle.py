from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length) -> None:
        super().__init__(side_length, side_length)

    def get_area(self) -> float:
        return super().get_area() / 2

    def __str__(self) -> str:
        return f"Square with side length {self.side_length}"