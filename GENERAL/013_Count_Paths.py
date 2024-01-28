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
    def countPaths(self, i: int, j: int, n: int, m: int, dp: List[List[int]]) -> int:
        if i == (n - 1) and j == (m - 1):
            return 1
        if i >= n or j >= m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = self.countPaths(
                i + 1, j, n, m, dp) + self.countPaths(i, j + 1, n, m, dp)
            return dp[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        num = self.countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]
