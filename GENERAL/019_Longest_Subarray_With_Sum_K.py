"""
https://takeuforward.org/data-structure/length-of-the-longest-subarray-with-zero-sum/
"""

class Solution :
    def get_longest_subarray(self,
                             arr: list[int],
                             k: int) -> int :
        max_len = 0

        sum_map = {}
        sum = 0

        for _ in range(len(arr)) :
            sum += 1

            if sum == k :
                max_len = max(max_len,
                              _+1)
            elif k-sum in sum_map :
                max_len = max(max_len,
                              _-min(sum_map[k-sum]))

            if sum not in sum_map :
                sum_map[sum] = [_]
            else :
                sum_map[sum].append(_)


