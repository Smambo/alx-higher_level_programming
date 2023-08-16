#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        result = []
        for element in matrix:
            row = []
            for num in element:
                row.append(num*num)
            result.append(row)
        return(result)
