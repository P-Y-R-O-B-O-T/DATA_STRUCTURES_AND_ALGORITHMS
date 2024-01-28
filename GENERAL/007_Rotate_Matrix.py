"""
https://leetcode.com/problems/rotate-image/
"""

"""
reverse the matrix and then take the transpose
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix)
        row_len = len(matrix[0])

        matrix = matrix[:::-1]

        for _ in range(matrix_len) :
            for __ in range(_, matrix_len) :
                matrix[_][__], matrix[__][_] = matrix[__][_], matrix[_][__]

        return matrix
