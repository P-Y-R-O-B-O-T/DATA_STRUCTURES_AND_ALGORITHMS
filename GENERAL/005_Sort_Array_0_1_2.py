"""
https://leetcode.com/problems/sort-colors/description/
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_ = {0: 0, 1: 0, 2: 0}
        for _ in nums :
            if _ in count_ :
                count_[_] += 1
        
        for _ in range(count_[0]) :
            nums[_] = 0
        for _ in range(count_[0], count_[0]+count_[1]) :
            nums[_] = 1
        for _ in range(count_[0]+count_[1], len(nums)) :
            nums[_] = 2
