import math

class RationalError(ZeroDivisionError):
    def __init__(self, message="знаменник не може дорівнювати нулю"):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message="невірне значення для операцій з Rational"):
        super().__init__(message)

class Rational:
    def __init__(self, a, b=None):
        if b is None:
            if isinstance(a, str):
                try:
                    num_str, den_str = a.split('/')
                    self.n = int(num_str)
                    self.d = int(den_str)
                except Exception as e:
                    raise RationalValueError("невірний формат рядка. Має бути 'n/d'") from e
            elif isinstance(a, Rational):
                self.n = a.n
                self.d = a.d
            else:
                raise RationalValueError("непідтримуваний тип аргументів")
        else:
            if isinstance(a, int) and isinstance(b, int):
                self.n = a
                self.d = b
            else:
                raise RationalValueError("чисельник і знаменник мають бути цілими числами")

        if self.d == 0:
            raise RationalError()
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
        raise RationalValueError("додавання можливе лише з типом int або Rational")

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
        raise RationalValueError("віднімання можливе лише з типом int або Rational")

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        raise RationalValueError("множення можливе лише з типом int або Rational")

    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                raise RationalError("ділення на нуль")
            other = Rational(other, 1)
        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError("ділення на нуль")
            return Rational(self.n * other.d, self.d * other.n)
        raise RationalValueError("ділення можливе лише з типом int або Rational")

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("ключ має бути 'n' для чисельника або 'd' для знаменника")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise RationalValueError("нове значення має бути цілим числом")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalError("знаменник не може бути 0")
            self.d = value
        else:
            raise KeyError("ключ має бути 'n' або 'd'")
        self._reduce()
