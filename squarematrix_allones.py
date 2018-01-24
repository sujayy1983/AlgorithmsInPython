"""
Author: Sujayyendhiren Ramarao Srinivasamurthi
Description: In a square matrix with a combination of zeros and ones. 
             Calculate largest square matrix with '1's

Referred good video: https://www.youtube.com/watch?v=aYnEO53H4lw
"""


import sys
import random
from collections import defaultdict


class Problem(object):
    """ General class that solves an algorithm ;) """
    def __init__(self, inpmatrix, resultmatrix, row, col):
        """
            inpmatrix: m*n matrix
        """
        self.row = row; self.col = col

        #----------------------------------#
        # Store original and result matrix #
        #----------------------------------#
        self.orgmatr = inpmatrix
        self.resmatr = resultmatrix

    def algorithm(self):
        """ Actual algorithm goes here """
        
        for row in range(1, self.row):
            for col in range(1, self.col):

                if self.orgmatr[row][col] == 0:
                    self.resmatr[row][col] = 0
                else:
                    self.resmatr[row][col] = min(self.orgmatr[row-1][col], \
                        self.orgmatr[row][col-1], self.orgmatr[row-1][col-1]) + 1

def generate_print_matrix(matrix, rowlen, colen, generate=True):
    """ Print and/or initialize matrices with some random input values """

    resultmatrix = None

    if generate:
        resultmatrix = defaultdict(dict)

    for row in range(rowlen):
        for col in range(colen):
            #---------------------------#
            # Generate only if required #
            #---------------------------#
            if generate == True:
                matrix[row][col] = random.randint(0, 1)
                if row == 0 or col == 0:
                    resultmatrix[row][col] = matrix[row][col]
                else:
                    resultmatrix[row][col] = 0
            sys.stdout.write(" {} ".format(matrix[row][col]))
        print(" ")
    return matrix, resultmatrix

if __name__ == "__main__":

    # ---------------- #
    # Test1 matrix n*n #
    # ---------------- #
    colen = 10; rowlen = 10

    print(" Initialized Matrix ".center(25))
    matrix, resmatrix = generate_print_matrix(defaultdict(dict), rowlen, colen)

    obj = Problem(matrix, resmatrix, rowlen, colen)
    obj.algorithm()

    print(" Result ".center(25))
    generate_print_matrix(obj.resmatr, rowlen, colen, generate=False)
