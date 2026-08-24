# Write a Python program to create a class that represents a shape. Include methods to calculate its 
# area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    """Subclass representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    """Subclass representing a square."""
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    """Subclass representing a triangle using its three sides."""
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Using Heron's formula to calculate area from 3 sides
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# --- Demonstration of the classes ---
if __name__ == "__main__":
    # Create instances of each shape
    circle = Circle(radius=5)
    square = Square(side=4)
    triangle = Triangle(side_a=3, side_b=4, side_c=5)

    # Display results
    print(f"Circle -> Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
    print(f"Square -> Area: {square.area():.2f}, Perimeter: {square.perimeter():.2f}")
    print(f"Triangle -> Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")
