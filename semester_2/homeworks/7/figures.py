import math

class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimetr(self):
        return None if self.dimention() == 3 else self._perimetr()

    def square(self):
        return None if self.dimention() == 3 else self._square()

    def squareSurface(self):
        return None if self.dimention() == 2 else self._squareSurface()

    def squareBase(self):
        return None if self.dimention() == 2 else self._squareBase()

    def height(self):
        return None if self.dimention() == 2 else self._height()

    def volume(self):
        return self._square() if self.dimention() == 2 else self._volume()

    def __str__(self):
        return self.__class__.__name__

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return 2

    def _perimetr(self):
        return self.a + self.b + self.c

    def _square(self):
        s = self._perimetr() / 2
        try:
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        except ValueError:
            return 0.0

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return 2

    def _perimetr(self):
        return 2 * (self.a + self.b)

    def _square(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle(a={self.a}, b={self.b})"

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def _perimetr(self):
        return 2 * math.pi * self.r

    def _square(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f"Circle(r={self.r})"

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3

    def _volume(self):
        return (4/3) * math.pi * self.r ** 3

    def __str__(self):
        return f"Ball(r={self.r})"

class Cone(Figure):
    def __init__(self, r, h):
        self.r, self.h = r, h

    def dimention(self):
        return 3

    def _volume(self):
        return (1/3) * math.pi * self.r ** 2 * self.h

    def __str__(self):
        return f"Cone(r={self.r}, h={self.h})"

def create_figure(name, params):
    try:
        if name == "Triangle":
            return Triangle(*params[:3])
        elif name == "Rectangle":
            return Rectangle(*params[:2])
        elif name == "Circle":
            return Circle(params[0])
        elif name == "Ball":
            return Ball(params[0])
        elif name == "Cone":
            return Cone(*params[:2])
    except Exception as e:
        print(f"Error creating {name} with params {params}: {e}")
        return None
