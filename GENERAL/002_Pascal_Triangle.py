"""
https://leetcode.com/problems/pascals-triangle/description/
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1 :
            return [[1]]
        if numRows == 2 :
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]

        for _ in range(numRows-2) :
            res.append([1])
            for __ in range(len(res[-2])-1) :
                res[-1].append(res[-2][__]+res[-2][__+1])
            res[-1].append(1)
        return res
