"""
https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=max_sum=nums[0]
        for _ in nums[1:] :
            curr_sum = max(_, curr_sum+_)
            max_sum = max(curr_sum, max_sum)
        return max_sum
