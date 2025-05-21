import math
import numpy as np

def gen_seq_a(x):
    term = 1.0
    k = 0
    while True:
        yield term
        k += 1
        term *= x * x / ((2 * k) * (2 * k - 1))

def compute_term_a(x, k):
    term = 1.0
    for i in range(1, k + 1):
        term *= x * x / ((2 * i) * (2 * i - 1))
    return term

def gen_seq_b():
    result = 1.0
    n = 1
    while True:
        result *= (1 + 1 / (n * n))
        yield result
        n += 1

def compute_product_b(n):
    result = 1.0
    for i in range(1, n + 1):
        result *= (1 + 1 / (i * i))
    return result

def build_matrix_c(n, a, b):
    M = np.zeros((n, n), dtype=float)
    for i in range(n):
        M[i, i] = a + b
        if i < n - 1:
            M[i, i + 1] = a * b
            M[i + 1, i] = 1
    return M

def compute_det_c(n, a, b):
    M = build_matrix_c(n, a, b)
    return float(np.linalg.det(M))

def gen_seq_c(a, b):
    n = 1
    while True:
        yield compute_det_c(n, a, b)
        n += 1

def gen_seq_d():
    a = [1, 1, 1]
    k = 1
    while True:
        if k <= 3:
            yield 1
        else:
            next_a = a[-1] + a[-3]
            a.append(next_a)
            yield next_a
        k += 1

def compute_sum_d(n):
    a = [0, 1, 1, 1]
    for k in range(4, n + 1):
        a.append(a[k - 1] + a[k - 3])
    return sum(a[k] / (2 ** k) for k in range(1, n + 1))

def gen_seq_e(x):
    m = 0
    while True:
        yield 2 * x ** (2 * m + 1) / (2 * m + 1)
        m += 1

def compute_taylor_e(x, epsilon=1e-6):
    total = 0.0
    m = 0
    while True:
        term = 2 * x ** (2 * m + 1) / (2 * m + 1)
        if abs(term) < epsilon:
            break
        total += term
        m += 1
    return total

def compare_math_e(x, epsilon=1e-6):
    approx = compute_taylor_e(x, epsilon)
    exact = math.log((1 + x) / (1 - x))
    return approx, exact

if __name__ == "__main__":
    x = 2.5
    k = 3
    print(f"{compute_term_a(x, k):.3}")
    print(f"{compute_product_b(k):.3}")
    print(f"{compute_det_c(k, 1.2, 0.7):.3}")
    print(f"{compute_sum_d(k):.3}")
    y_approx, y_exact = compare_math_e(0.5)
    print(f"{y_approx:.3}", f"{y_exact:.3}")