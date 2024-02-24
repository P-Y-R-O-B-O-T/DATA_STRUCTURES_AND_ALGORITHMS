"""
https://takeuforward.org/data-structure/minimum-number-of-platforms-required-for-a-railway/
"""

class Solution :
    def min_platforms(self,
                      arr: list[int],
                      dep: list[int]) -> int :
        if arr == [] : return 0

        dep_stack = [dep[0]]
        platforms = 1
        max_platforms = 1

        for _ in range(1, len(arr)) :
            if arr[_] >= dep_stack[-1] :
                while arr[_] >= dep_stask[-1] :
                    dep_stack.pop(-1)
                    platforms -= 1
            
            if arr[_] < dep_stack[-1] :
                dep_stack.append(dep[_])
                platforms += 1

            max_platforms = max(max_platforms,
                                platforms)

        return max_platforms
