import numpy as np

class Matrix2D:
    def __init__(self, a, b, c, d):
        self.matrix = np.array([[a, b], [c, d]])

    def determinant(self):
        return np.linalg.det(self.matrix)

    def is_singular(self):
        return self.determinant() == 0

class Vector2D:
    def __init__(self, x, y):
        self.vector = np.array([x, y])

class Solver:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    def solve(self):
        if self.matrix.is_singular():
            return None
        return np.linalg.solve(self.matrix.matrix, self.vector.vector)

def read_data(matrix_file, vector_file):
    with open(matrix_file, 'r') as mf, open(vector_file, 'r') as vf:
        matrices = [list(map(int, line.split())) for line in mf]
        vectors = [list(map(int, line.split())) for line in vf]
    return matrices, vectors

