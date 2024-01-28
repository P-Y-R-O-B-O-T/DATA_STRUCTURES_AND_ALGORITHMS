"""
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        row_start = 0
        row_end = len(matrix) - 1

        while row_start <= row_end :
            mid = (row_start + row_end)//2
            if matrix[mid][0] <= target <= matrix[mid][-1] :
                row = mid
                break
            if matrix[mid][-1] < target :
                row_start = mid + 1
            elif matrix[mid][0] > target :
                row_end = mid - 1

        if row < 0 :
            return False

        start = 0
        end = len(matrix[row]) - 1
        while start <= end :
            mid = (start + end)//2
            if matrix[row][mid] < target : start = mid + 1
            elif matrix[row][mid] > target : end = mid - 1
            elif target == matrix[row][mid] : return True
        return False
