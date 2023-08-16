#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        if len(matrix) == 0:
            return None
        result = []
        for element in matrix:
            row = []
            for num in element:
                row.append(num*num)
            result.append(row)
        return(result)
