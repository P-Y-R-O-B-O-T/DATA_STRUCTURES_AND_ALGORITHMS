"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution :
    def get_lcs(self, arr: list[int]) -> int :
        arr.sort()

        if arr == [] : return 0
        if len(arr) == 1 : return 1

        max_len = 1
        curr_len = 1

        for _ in range(1, len(arr)) :
            if arr[_] > arr[_-1] :
                curr_len += 1
                max_len = max(max_len, curr_len)
            elif arr[_] == arr[_-1] :
                pass
            else :
                curr_len = 1
        return curr_len
