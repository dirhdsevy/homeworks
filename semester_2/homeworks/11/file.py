import math

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
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = a + b
        if i < n - 1:
            matrix[i][i + 1] = a * b
            matrix[i + 1][i] = 1.0
    return matrix

def compute_determinant(matrix):
    n = len(matrix)
    det = 1.0
    for i in range(n):
        pivot = matrix[i][i]
        if pivot == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    det *= -1
                    pivot = matrix[i][i]
                    break
        det *= pivot
        for j in range(i + 1, n):
            factor = matrix[j][i] / pivot
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
    return det

def compute_det_c(n, a, b):
    matrix = build_matrix_c(n, a, b)
    return compute_determinant(matrix)

def gen_seq_c(a, b):
    order = 1
    while True:
        yield compute_det_c(order, a, b)
        order += 1

def gen_seq_d():
    seq = [1, 1, 1]
    k = 1
    while True:
        if k <= 3:
            yield 1
        else:
            next_val = seq[-1] + seq[-3]
            seq.append(next_val)
            yield next_val
        k += 1

def compute_sum_d(n):
    seq = [0, 1, 1, 1]
    for k in range(4, n + 1):
        seq.append(seq[k - 1] + seq[k - 3])
    return sum(seq[k] / (2 ** k) for k in range(1, n + 1))

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