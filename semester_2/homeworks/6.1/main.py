from matrix_solver_storozhuk import Matrix2D, Vector2D, Solver

def read_data(matrix_file, vector_file):
    with open(matrix_file, 'r') as mf, open(vector_file, 'r') as vf:
        matrices = [list(map(int, line.split())) for line in mf]
        vectors = [list(map(int, line.split())) for line in vf]
    return matrices, vectors

def main():
    matrices, vectors = read_data("matrix_coefficients.txt", "rhs_values.txt")
    for (a, b, c, d), (x, y) in zip(matrices, vectors):
        solution = Solver(Matrix2D(a, b, c, d), Vector2D(x, y)).solve()
        print(solution if solution is not None else "No solution")

if __name__ == "__main__":
    main()
