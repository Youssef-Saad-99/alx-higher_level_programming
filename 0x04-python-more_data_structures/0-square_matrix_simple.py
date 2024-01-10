#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[num**2 for num in row] for row in matrix]
    return result_matrix
