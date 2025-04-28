ex = input("Введіть номер задачі(a, b, c): ")
N = int(input("Введіть номер числа до якого ви хочете знайти суму: "))

def factorial(f):
    a = 1
    for i in range(1, f+1):
        a *= i
    return a

def func_a(N):
    pn = 0

    for i in range(2, N+1):
        pn *= (1-(1/(i**2)))

    yield (f"{pn:.3f}")

def func_b(N):
    pn = 0

    for i in range(1, N+1):
        pn *= 2 + (1/factorial(i))

    yield (f"{pn:.3f}")

def func_c(N):
    pn = 0

    for i in range(1, N+1):
        pn *= (i+1)/(i+2)

    yield (f"{pn:.3f}")


if ex == "a":
    for value in func_a(N):
        print(value)

elif ex == "b":
    for value in func_b(N):
        print(value)

elif ex == "c":
    for value in func_c(N):
        print(value)