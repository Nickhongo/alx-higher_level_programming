#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix 
    
    """
    if type(matrix) is list:
        for item in matrix:
            if type(item) is list:
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError(
                                "matrix must be a matrix (list of lists)"
                                " of integers/floats"
                                )
            else:
                raise TypeError(
                        "matrix must be a matrix (list of lists) of" +
                        " of integers/floats"
                        )
    else:
        raise TypeError(
                "matrix must be a matrix (list of lists) of" +
                " integers/floats"
                )
                        
    sizes = []
    for item in matrix:
        sizes.append(len(item))

    len1 = sizes[0]
    for size in sizes:
        if size == len1:
            continue
        else:
            raise TypeError(
                    "Each row of the matric must have the same size"
                    )
    if isinstance(div, (int, float)):
        if div == 0:
            raise ZeroDivisionError("divisionn by zero")
    else:
        raise TypeError("div must be a number")

    mat = matrix.copy()
    return list(
            map(lambda row: list(map(lambda x: round(x / div, 2), row)), mat
                ))
