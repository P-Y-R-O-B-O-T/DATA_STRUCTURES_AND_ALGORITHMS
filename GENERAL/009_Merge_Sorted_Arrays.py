"""
https://leetcode.com/problems/merge-sorted-array/description/
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        pointer = len(nums1)-1

        for _ in range(len(nums2)-1, -1, -1) :
            nums1[pointer] = nums2[_]
            pointer -= 1
        
        nums1.sort()
