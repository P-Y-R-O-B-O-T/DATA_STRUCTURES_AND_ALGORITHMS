"""
https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for _ in range(len(nums)-1) :
            if nums[_] == nums[_+1] :
                return nums[_]


"""
Use this approach when a number is twice only and rest are fine
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ideal_sum = int(len(nums)*(len(nums)+1)/2) # from ap sum formula
        curr_sum = sum(nums)
        number = len(nums) - (ideal_sum-curr_sum)
        print(ideal_sum, curr_sum, ideal_sum^curr_sum, number)
        return number
