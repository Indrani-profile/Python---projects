import math

class Square:
    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def area(self):
        return self.side * self.side

    @property
    def diagonal(self):
        return math.sqrt(2 * self.side ** 2)

square = Square(5)

print(f"Side: {square.side}")
print(f"Perimeter: {square.perimeter}")
print(f"Area: {square.area}")
print(f"Diagonal: {square.diagonal}")