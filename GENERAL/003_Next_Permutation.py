"""
https://leetcode.com/problems/next-permutation/description/
"""

"""
iterate over the given array from end and find the first index (pivot) which doesn’t follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1])

Check if pivot index does not exist
        This means that the given sequence in the array is the largest as possible.
        So, swap the complete array

Otherwise, Iterate the array from the end and find for the successor of pivot in suffix

Swap the pivot and successor

Minimize the suffix part by reversing the array from pivot + 1 till N
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        j = n-1

        while i >= 0 :
            if nums[i] < nums[i+1] :
                break
            i -= 1
        
        if i < 0 :
            nums.reverse()
        else :
            while j > i :
                if nums[j] > nums[i] :
                    break
                j -= 1
            
            nums[j], nums[i] = nums[i], nums[j]

            nums[i+1:] = nums[i+1:][::-1]
        
        return nums
