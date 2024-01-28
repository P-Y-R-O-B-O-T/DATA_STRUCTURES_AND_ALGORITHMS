"""
https://leetcode.com/problems/powx-n/description/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 : return 1/self.pow(x, -n)
        return self.pow(x, n)


    def pow(self, x, n) :
        if n == 0 : return 1
        if n % 2 == 0 :
            return self.pow(x*x, n//2)
        else : return x*self.pow(x*x, (n-1)//2)
