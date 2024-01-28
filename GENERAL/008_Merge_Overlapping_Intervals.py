"""
https://leetcode.com/problems/merge-intervals/
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=self.sort_key)

        res = [intervals[0]]

        for _ in range(1, len(intervals)) :
            if intervals[_][0] <= res[-1][1] :
                res[-1][1] = max(intervals[_][1], res[-1][1])
            else :
                res.append(intervals[_])
        
        return res
    
    def sort_key(self, data) :
        return data[0]
