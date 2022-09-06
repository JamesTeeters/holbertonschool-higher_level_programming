#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cp = []
    for i in range(len(matrix)):
        row = map(lambda n: n * n, matrix[i])
        matrix_cp.append(list(row))
    return matrix_cp
