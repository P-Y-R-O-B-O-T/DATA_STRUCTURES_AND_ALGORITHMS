"""
https://leetcode.com/problems/4sum/description/
"""

class Solution :
    def four_sum(self,
                 arr: list[int],
                 target: int) -> list[list[int]] :
        arr.sort()
        ans = []

        for _ in range(len(arr)-3) :
            for __ in arr[_+1, len(arr)-2] :
                start = __+1
                end = len(arr) - 1

                while start < end :
                    s = arr[_] + arr[__] + arr[start] + arr[end]
                    if s == target :
                        ans.append([_, __, start, end])

                        while left < right and arr[start] == arr[start+1] :
                            left += 1
                        while right > left and arr[right] == arr[right-1] :
                            right -= 1
                        left += 1
                        right -= 1
                    if s < target :
                        start += 1
                    if s > target :
                        end -= 1

        return ans
