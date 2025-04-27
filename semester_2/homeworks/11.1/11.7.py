from ctypes import c_ulong

ex = input("Введіть номер задачі(a, b, c, d): ")
x = float(input("Введіть перший член послідовності: "))
n = int(input("Введіть порядковий номер шуканого числа: "))

def factorial(f):
    a = 1
    for i in range(1, f+1):
        a *= i
    return a


def func_a(x):
    xk = x

    for k in range(1, n+1):
        xk *= (x**2)/(2*k * (2*k+1))
        yield(f"{xk:.3f}")

def func_b(x):
    xk = -x

    for k in range(1, n+1):
        xk *= (x-x*k)/k
        yield(f"{xk:.3f}")

def func_c(x):
    xk = 1

    for k in range(1, n+1):
        xk *= (-x*factorial((k**2-k)))/factorial(k**2+k)
        yield(f"{xk:.3f}")

def func_d(x):
    xk = 1

    for k in range(1, n+1):
        xk *= (k*x + x)/k
        yield(f"{xk:.3f}")

if ex == "a":
    for value in func_a(x):
        print(value)

elif ex == "b":
    for value in func_b(x):
        print(value)

elif ex == "c":
    for value in func_c(x):
        print(value)

elif ex == "d":
    for value in func_d(x):
        print(value)


