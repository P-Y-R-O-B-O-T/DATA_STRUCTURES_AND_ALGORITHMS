"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float("inf")
        max_prof = 0
        for _ in prices :
            if _ < min_ :
                min_ = _
            max_prof = max(max_prof, _-min_)
        return max_prof
