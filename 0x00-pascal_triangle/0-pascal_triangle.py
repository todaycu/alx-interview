#!/usr/bin/python3

"""
Calculates integers representing the Pascal's triangle of n

Args:
    n (int): number of lines in a Pascal's triangle
    
Returns:
    list: a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Calculate pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(1, n+1):
            C = 1
            tmp = []
            for j in range(1, i+1):
                tmp.append(C)
                C = C * (i - j) // j
            triangle.append(tmp)
    return triangle
