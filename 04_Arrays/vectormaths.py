# Module vectormath performs vector operations on 3D vectors
# Bonga Njamela [NJMLUN002]
# 02/06/20

import math

def vector_sum(A,B):
    """Function returns the vector sum of vector A and B"""
    C = []
    for i in range(3):
        C.append(A[i]+B[i])
    return C

def vector_product(A,B):
    """Function returns the dot product of vector A and B"""
    C = []
    for i in range(3):
        C.append(A[i]*B[i])
    return C

def vector_norm(A):
    """Function returns the length of a vector A""" 
    norm = 0
    comp_sqrd = 0
    under_sqrt = 0
    for i in range(3): 
        comp_sqrd = A[i]**2
        under_sqrt += comp_sqrd
    norm = math.sqrt(under_sqrt)
    return norm