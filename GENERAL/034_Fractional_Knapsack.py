"""
https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/
"""

"""
inp = [[value, weight], ...]
"""

class Solution :
    def knapsack(self,
                 inp: list[list[int]],
                 max_weight: int) -> int :
        for _ in range(len(inp)) :
            inp.append(inp[_][0]/inp[_][1])
        inp.sort(key=sorting_criteria)

        weight = 0
        profit = 0

        for _ in inp :
            if _[1]+weight > max_weight :
                profit += _[2]*(max_weight-weight)
                break
            else :
                profit += _[0]

        return profit

    def sorting_criteria(self, item) :
        return item[2]
