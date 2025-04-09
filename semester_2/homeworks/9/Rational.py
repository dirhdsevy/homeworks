import math

class Rational:
    def __init__(self, a, b=None):
        if b is None:
            if isinstance(a, str):
                try:
                    num_str, den_str = a.split('/')
                    self.n = int(num_str)
                    self.d = int(den_str)
                except Exception as e:
                    raise ValueError("Невірний формат рядка Має бути 'n/d'") from e
            elif isinstance(a, Rational):
                self.n = a.n
                self.d = a.d
            else:
                raise ValueError("Непідтримуваний тип аргументів")
        else:
            if isinstance(a, int) and isinstance(b, int):
                self.n = a
                self.d = b
            else:
                raise ValueError("Чисельник і знаменник мають бути цілими числами")
        if self.d == 0:
            raise ZeroDivisionError("Знаменник не може дорівнювати нулю")
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        self._reduce()
    def _reduce(self):
        g = math.gcd(self.n, self.d)
        if g:
            self.n //= g
            self.d //= g
    def __str__(self):
        return f"{self.n}/{self.d}"
    def __repr__(self):
        return f"Rational({self.n}, {self.d})"
    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
        raise TypeError("Додавання можливе лише з типом int або Rational")
    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
        raise TypeError("Віднімання можливе лише з типом int або Rational")
    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        raise TypeError("Множення можливе лише з типом int або Rational")
    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Ділення на нуль")
            other = Rational(other, 1)
        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError("Ділення на нуль")
            return Rational(self.n * other.d, self.d * other.n)
        raise TypeError("Ділення можливе лише з типом int або Rational")
    def __call__(self):
        return self.n / self.d
    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Ключ має бути 'n' для чисельника або 'd' для знаменника")
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Нове значення має бути цілим числом")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Знаменник не може бути 0")
            self.d = value
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")
        self._reduce()

def evaluate_expr(expr: str) -> Rational:
    expr = expr.replace(" ", "")
    pos = 0
    def parse_number():
        nonlocal pos
        start = pos
        while pos < len(expr) and (expr[pos].isdigit() or expr[pos] == '/'):
            pos += 1
        s = expr[start:pos]
        return Rational(s) if '/' in s else Rational(int(s), 1)
    def parse_factor():
        return parse_number()
    def parse_term():
        nonlocal pos
        result = parse_factor()
        while pos < len(expr) and expr[pos] == '*':
            pos += 1
            result = result * parse_factor()
        return result
    def parse_expression():
        nonlocal pos
        result = parse_term()
        while pos < len(expr) and expr[pos] in '+-':
            op = expr[pos]
            pos += 1
            right = parse_term()
            result = result + right if op == '+' else result - right
        return result
    return parse_expression()

if __name__ == "__main__":
    expressions = [
        "4 - 92 - 79 * 59 * 90/16 * 75 - 55 * 82/41 * 19",
        "48 + 74/40 * 64 * 93/50 * 52/77 * 57 * 45/95 * 30 * 77/20 * 74 * 59/27 + 29 + 18 * 84/19 - 84/73 + 56/66 - 62 - 99 + 9 * 8 + 71/19 * 51 * 35 * 29 + 86/80 + 45 * 42 * 92 * 98/78 * 33/92 + 70",
        "9 * 40 + 96 * 83 - 43 - 69 + 12 * 48/65 * 10 - 90"
    ]
    for i, expr in enumerate(expressions, start=1):
        try:
            result = evaluate_expr(expr)
            dec_value = result()
            print(f"Вираз {i}: {expr}")
            print(f"  Результат у вигляді дробу: {result}")
            print(f"  Десятковий результат: {dec_value:.3f}\n")
        except Exception as e:
            print(f"Помилка в обчисленні виразу: {i} {e}\n")
