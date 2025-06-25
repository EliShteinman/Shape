from shape.circle import Circle
from shape.rectangle import Rectangle
from shape.square import Square
from shape.hexagon import Hexagon
from shape.rightAngledTriangle import RightAngledTriangle


def demonstrate_equality():
    """Demonstrates the power of the __eq__ method."""
    print("--- 1. Demonstrating Equality (__eq__) ---")

    # Create pairs of shapes that should be considered equal
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(20, 10)  # Flipped dimensions
    print(f"Is {rect1} equal to {rect2}? -> {rect1 == rect2}")

    tri1 = RightAngledTriangle(3, 4)
    tri2 = RightAngledTriangle(4, 3)  # Flipped dimensions
    print(f"Is {tri1} equal to {tri2}? -> {tri1 == tri2}")

    # Create a shape that should NOT be equal
    rect3 = Rectangle(10, 21)
    print(f"Is {rect1} equal to {rect3}? -> {rect1 == rect3}\n")


def demonstrate_sorting_and_comparison():
    """Demonstrates sorting (__lt__) and the power of @total_ordering."""
    print("--- 2. Demonstrating Comparison & Sorting (__lt__, @total_ordering) ---")

    # Create a list of shapes with some interesting areas
    shapes = [
        Square(10),  # Area: 100
        Rectangle(10, 5),  # Area: 50
        Circle(5.64),  # Area: ~100
        Rectangle(5, 10),  # Area: 50 (should be equal to the other 10x5)
        RightAngledTriangle(10, 20),  # Area: 100
        Hexagon(8),  # Area: ~166
        Square(7.071)  # Area: ~50
    ]

    print("Original list of shapes:")
    for shape in shapes:
        print(f"  - {shape} (Area: {shape.get_area():.2f})")

    # Sorting will work automatically thanks to __lt__ and @total_ordering
    shapes.sort()

    print("\nSorted list of shapes (by area):")
    for shape in shapes:
        print(f"  - {shape} (Area: {shape.get_area():.2f})")

    # Demonstrate all comparison operators
    shape_a = Square(5)  # Area 25
    shape_b = Circle(4)  # Area ~50.26
    print("\nFurther comparisons:")
    print(f"Is {shape_a} < {shape_b}? -> {shape_a < shape_b}")
    print(f"Is {shape_a} > {shape_b}? -> {shape_a > shape_b}")
    print(f"Is {shape_a} >= {shape_b}? -> {shape_a >= shape_b}\n")


def demonstrate_math_operations():
    """Demonstrates mathematical operations __add__ and __mul__."""
    print("--- 3. Demonstrating Math Operations (__add__, __mul__) ---")

    base_rect = Rectangle(4, 5)  # Area: 20
    base_circ = Circle(3)  # Area: ~28.27

    # Demonstrate __add__
    total_area = base_rect + base_circ
    print(f"Adding areas: Area of {base_rect} + Area of {base_circ} = {total_area:.2f}")

    # Demonstrate __mul__ (scaling)
    print(f"\nOriginal shape: {base_rect} (Area: {base_rect.get_area():.2f})")

    scaled_up = base_rect * 3
    print(f"Scaled up by 3: {scaled_up} (Area: {scaled_up.get_area():.2f})")

    scaled_down = base_rect * 0.5
    print(f"Scaled down by 0.5: {scaled_down} (Area: {scaled_down.get_area():.2f})\n")


def main():
    """
    Main module to showcase the full power of the shape classes.
    """
    demonstrate_equality()
    demonstrate_sorting_and_comparison()
    demonstrate_math_operations()


# Run the main function only when the script is executed directly
if __name__ == "__main__":
    main()