import math
from figures.base import Figure
from figures.two_d import Triangle, Rectangle

class Ball(Figure):
    def __init__(self, r):
        self.r = r
    def dimension(self):
        return 3
    def volume(self):
        return (4/3) * math.pi * self.r ** 3
    def __str__(self):
        return f"Ball({self.r})"

class TriangularPyramid(Triangle):
    def __init__(self, side, height):
        super().__init__(side, side, side)
        self.h = height
    def dimension(self):
        return 3
    def squareBase(self):
        return self.square()
    def volume(self):
        return (1/3) * self.square() * self.h
    def __str__(self):
        return f"TriangularPyramid({self.a}, {self.h})"

class QuadrangularPyramid(Rectangle):
    def __init__(self, side1, side2, height):
        super().__init__(side1, side2)
        self.h = height
    def dimension(self):
        return 3
    def squareBase(self):
        return self.square()
    def volume(self):
        return (1/3) * self.square() * self.h
    def __str__(self):
        return f"QuadrangularPyramid({self.a}, {self.b}, {self.h})"

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimension(self):
        return 3
    def volume(self):
        return self.a * self.b * self.c
    def __str__(self):
        return f"RectangularParallelepiped({self.a}, {self.b}, {self.c})"

class Cone(Figure):
    def __init__(self, r, height):
        self.r, self.h = r, height
    def dimension(self):
        return 3
    def volume(self):
        return (1/3) * math.pi * self.r ** 2 * self.h
    def __str__(self):
        return f"Cone({self.r}, {self.h})"

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, height):
        super().__init__(a, b, c)
        self.h = height
    def dimension(self):
        return 3
    def volume(self):
        return self.square() * self.h
    def __str__(self):
        return f"TriangularPrism({self.a}, {self.b}, {self.c}, {self.h})"
