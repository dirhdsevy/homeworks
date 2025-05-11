from Rational import Rational, RationalValueError

class RationalList:
    def __init__(self, elements=None):
        self.data = []
        if elements is not None:
            for e in elements:
                self.append(e)

    def append(self, value):
        if isinstance(value, int):
            value = Rational(value, 1)
        elif not isinstance(value, Rational):
            raise RationalValueError("До списку можна додавати лише Rational або int")
        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value, 1)
        elif not isinstance(value, Rational):
            raise RationalValueError("До списку можна присвоювати лише Rational або int")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        result = RationalList(self.data)
        if isinstance(other, RationalList):
            for v in other:
                result.append(v)
        elif isinstance(other, (int, Rational)):
            result.append(other)
        else:
            raise RationalValueError("можна додавати тільки RationalList або число")
        return result

    def __radd__(self, other):
        if isinstance(other, (int, Rational)):
            return RationalList([other]) + self
        raise RationalValueError("можна додавати тільки RationalList або число")

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for v in other:
                self.append(v)
        elif isinstance(other, (int, Rational)):
            self.append(other)
        else:
            raise RationalValueError("можна додавати тільки RationalList або число")
        return self

    def __iter__(self):
        sorted_data = sorted(self.data, key=lambda x: (-x.d, -x.n))
        return iter(sorted_data)
