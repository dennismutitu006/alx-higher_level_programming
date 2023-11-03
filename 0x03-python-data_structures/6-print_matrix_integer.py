#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for trix in mat:
            print("{:d}".format(trix), end=" " if trix != mat[-1] else "")
            print()
