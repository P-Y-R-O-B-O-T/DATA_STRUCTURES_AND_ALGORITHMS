"""
https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/
"""

class Solution :
    def get_sequenced_jobs(self,
                           jobs: list[list[int]]) -> int :
        jobs.sort(key=self.sort_criteria,
                  reverse=True)
        map = {}
        sum = 0
        for _ in range(len(jobs)) :
            if jobs[_][1] not in map :
                map[job[_][1]] = jobs[_][2]
                sum += jobs[_][2]
            else :
                for __ in range(1, job[_][1]) :
                    if __ not in map :
                        map[__] = jobs[_][2]
                        sum += jobs[_][2]
        return sum

    def sort_criteria(self,
                      item: list[int]) -> int :
        return item[2]
