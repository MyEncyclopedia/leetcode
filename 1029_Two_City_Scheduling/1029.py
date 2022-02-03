# Runtime: 36 ms, faster than 87.77% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 14.5 MB, less than 14.84% of Python3 online submissions for Two City Scheduling.
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        L = range(len(costs))
        cost_diff_lst = [(i, costs[i][0] - costs[i][1]) for i in L]
        cost_diff_lst.sort(key=lambda x: x[1])

        total_cost = 0
        for c, (idx, _) in enumerate(cost_diff_lst):
            is_left = 0 if c < len(L) // 2 else 1
            total_cost += costs[idx][is_left]

        return total_cost


if __name__ == "__main__":
    s = Solution()
    # costs = [[10,20],[30,200],[400,50],[30,20]]
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]

    print(s.twoCitySchedCost(costs))

