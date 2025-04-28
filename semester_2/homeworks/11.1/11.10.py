n = int(input("Введіть номер числа до якого ви хочете знайти суму: "))

def fraction():
    result = 4 * n + 2
    for k in range(n - 1, 0, -1):
        result = 4 * k + 2 + 1 / result
    result = 2 + 1 / result

    yield result

for value in fraction():
    print(value)