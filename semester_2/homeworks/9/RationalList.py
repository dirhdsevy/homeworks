from Rational import Rational


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
            raise TypeError("допустимі тільки int або Rational")
        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value, 1)
        elif not isinstance(value, Rational):
            raise TypeError("допустимі тільки int або Rational")
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
            raise TypeError("можна додавати тільки RationalList або число")
        return result

    def __radd__(self, other):
        if isinstance(other, (int, Rational)):
            return RationalList([other]) + self
        raise TypeError("можна додавати тільки RationalList або число")

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for v in other:
                self.append(v)
        elif isinstance(other, (int, Rational)):
            self.append(other)
        else:
            raise TypeError("можна додавати тільки RationalList або число")
        return self

    def __iter__(self):
        sorted_data = sorted(self.data, key=lambda x: (-x._denominator, -x._numerator))
        return iter(sorted_data)


def parse_rational(s):
    s = s.strip()
    if '/' in s:
        return Rational(s)
    return Rational(int(s), 1)


def read_rational_list(filename):
    lst = RationalList()
    with open(filename, encoding='utf-8') as f:
        for line in f:
            for part in line.split():
                lst.append(parse_rational(part))
    return lst


def sum_rational_list(lst):
    result = Rational(0, 1)
    for r in lst:
        result = result + r
    return result


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for fname in files:
        try:
            rl = read_rational_list(fname)
            print(f"\n{fname}:")
            for r in rl:
                print(r, end=" ")
            s = sum_rational_list(rl)
            print(f"\nSum: {s} ({s()})")
        except Exception as e:
            print(f"{fname} {e}")