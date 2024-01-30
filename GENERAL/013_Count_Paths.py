"""
https://leetcode.com/problems/unique-paths/description/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.sols = 0
        self.m = m
        self.n = n
        self.find_solution(0, 0)
        return self.sols

    def find_solution(self, x: int, y: int) :
        if x >= self.m or y >= self.n :
            return

        if x == self.m - 1 and y == self.n - 1 :
            self.sols += 1

        if x + 1 < self.m :
            self.find_solution(x+1, y)
        if y + 1 < self.n :
            self.find_solution(x, y+1)


"""
dp solution
"""
class Solution:
    def countPaths(self,
                   i: int,
                   j: int,
                   n: int,
                   m: int) -> int :
        dp = [0 for _ in range(n) for __ in range(m)]

        for _ in range(m) :
            dp[_][0] = 1
        for _ in range(n) :
            do[0][_] = 1

        for _ in range(1, m) :
            for __ in range(1, n) :
                dp[_][__] = dp[_-1][__] + dp[_][__-1]

        return dp[m-1][n-1]
