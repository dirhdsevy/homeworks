ex = input("Введіть номер задачі(a, b, c): ")
N = int(input("Введіть номер числа до якого ви хочете знайти суму: "))

def func_a(N):
    sn = 0

    for n in range(1, N+1):
        sn += n*(-1)**(n+1)

    yield (f"{sn:.3f}")

def func_b(N):
    sn = 0

    for n in range(2, N+1):
        sn += 1/((n-1)*n)

    yield (f"{sn:.3f}")

def func_c(N):
    sn = 0

    for n in range(1, N+1):
        sn += (((-1)**n)*(n-1)) / n

    yield (f"{sn:.3f}")


if ex == "a":
    for value in func_a(N):
        print(value)

elif ex == "b":
    for value in func_b(N):
        print(value)

elif ex == "c":
    for value in func_c(N):
        print(value)