import math

class Figure:
    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if not self.is_valid():
            return 0
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle(a={self.a}, b={self.b})"

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        diff = abs(self.b - self.a)
        if diff == 0:
            return None
        x = ((diff ** 2 + self.c ** 2 - self.d ** 2) / (2 * diff))
        h_squared = self.c ** 2 - x ** 2
        h = math.sqrt(h_squared) if h_squared > 0 else 0
        return (self.a + self.b) / 2 * h

    def __str__(self):
        return f"Trapeze(a={self.a}, b={self.b}, c={self.c}, d={self.d})"

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def __str__(self):
        return f"Parallelogram(a={self.a}, b={self.b}, h={self.h})"

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f"Circle(r={self.r})"

def read_figures_from_file(filename):
    figures = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if not parts:
                    continue
                figure_name = parts[0]
                try:
                    params = list(map(float, parts[1:]))
                except ValueError:
                    continue
                if figure_name == "Triangle" and len(params) == 3:
                    figures.append(Triangle(*params))
                elif figure_name == "Rectangle" and len(params) == 2:
                    figures.append(Rectangle(*params))
                elif figure_name == "Trapeze" and len(params) == 4:
                    figures.append(Trapeze(*params))
                elif figure_name == "Parallelogram" and len(params) == 3:
                    figures.append(Parallelogram(*params))
                elif figure_name == "Circle" and len(params) == 1:
                    figures.append(Circle(*params))
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    return figures
