import math
from figures.base import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def dimension(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        s = self.perimetr() / 2
        try:
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        except:
            return 0
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def dimension(self):
        return 2
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"

class Trapeze(Figure):
    def __init__(self, base1, base2, lateral1, lateral2):
        self.base1, self.base2 = base1, base2
        self.lateral1, self.lateral2 = lateral1, lateral2
    def dimension(self):
        return 2
    def perimetr(self):
        return self.base1 + self.base2 + self.lateral1 + self.lateral2
    def _height(self):
        a = min(self.base1, self.base2)
        b = max(self.base1, self.base2)
        c, d = self.lateral1, self.lateral2
        if b == a:
            return c
        try:
            expr = ((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))
            return math.sqrt(c ** 2 - expr ** 2)
        except:
            return 0
    def square(self):
        return ((self.base1 + self.base2) / 2) * self._height()
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Trapeze({self.base1}, {self.base2}, {self.lateral1}, {self.lateral2})"

class Parallelogram(Figure):
    def __init__(self, side, side2, height):
        self.side, self.side2, self.h = side, side2, height
    def dimension(self):
        return 2
    def perimetr(self):
        return 2 * (self.side + self.side2)
    def square(self):
        return self.side * self.h
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Parallelogram({self.side}, {self.side2}, {self.h})"

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def dimension(self):
        return 2
    def perimetr(self):
        return 2 * math.pi * self.r
    def square(self):
        return math.pi * self.r ** 2
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Circle({self.r})"
