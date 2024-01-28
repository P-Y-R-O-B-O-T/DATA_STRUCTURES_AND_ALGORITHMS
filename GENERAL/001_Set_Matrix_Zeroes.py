"""
https://leetcode.com/problems/set-matrix-zeroes/description/
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        matrix_len = len(matrix)
        row_len = len(matrix[0])

        cols_zero = {}
        rows_zero = {}

        for _ in range(matrix_len) :
            if 0 in matrix[_] :
                rows_zero[_] = _
            for __ in range(row_len) :
                if matrix[_][__] == 0 :
                    cols_zero[__] = __
        
        for _ in rows_zero :
            matrix[_] = [0]*row_len
        
        for _ in cols_zero :
            for __ in range(matrix_len) :
                if __ not in rows_zero :
                    matrix[__][_] = 0
