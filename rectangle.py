from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width:float = width
        self.height:float = height

    def get_area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"