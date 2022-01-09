""" Module which contains functions to do matrix math.
"""
import math
import random
import numpy as np

def get_matrix(n):
    # Create placeholder n x n matrix.
    mtrx = []
    for row in range(n):
        new_list = []
        mtrx.append(new_list)
        for col in range(n):
            mtrx[row].append(0)
    return mtrx

def input_value():
    legal = False
    while not legal:
        try: 
            val = int(input("Please enter a value: "))
            float(val)
            legal = True
        except:
            print("Error. Only integers may be entered.")
    return val
            
def fill_matrix(a):
    """Fill in the values of the matrix.
        Params: 
            a: an n x n matrix. 
    """
    # Fill in the entries of the matrix.
    # This model assumes that entries are nxn.
    n = len(a)
    for y in range(n):
        for x in range(n):
            a[y][x] = int(random.randint(0,1))

def user_fill_matrix(a):
    """Fill in the values of the matrix.
        Params: 
            a: an n x n matrix. 
    """
    # Fill in the entries of the matrix.
    # This model assumes that entries are nxn.
    n = len(a)
    for y in range(n):
        for x in range(n):
            a[y][x] = input_value()

def matrix_print(a):
    """Special print to show matricity.
        a: a matrix
    """
    for row in a:
        print(row)

def matrix_addition(a,b):
    """ Add 2 metrices together. 
    Assumes that parameters are valid!!!!!
    a, b: nxn matrices
    """
    # Create 'housing' for answer.
    result = get_matrix(len(a))
    # Pretty print 
    matrix_print(a)
    print("+")
    matrix_print(b)
    print("=")
    # Add matrices together and add to result.
    n = len(a)
    for x in range(n):
        for y in range(n):
            sum = a[x][y] + b[x][y]
            result[x][y] = sum
    matrix_print(result)
    return result

def main():
    
    # present three options
    # input : pick what u want to do 
    # if choice 1,2,3 then func.

main()

