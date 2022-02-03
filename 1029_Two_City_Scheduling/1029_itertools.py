# Time Limit Exceeded
import math
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        L = range(len(costs))
        from itertools import combinations
        left_set_list = [set(c) for c in combinations(list(L), len(L)//2)]

        min_total = math.inf
        for left_set in left_set_list:
            cost = 0
            for i in L:
                is_left = 1 if i in left_set else 0
                cost += costs[i][is_left]
            min_total = min(min_total, cost)

        # for left_set in left_set_list:
        #     cost = sum([(lambda x: costs[x][0] if x in left_set else costs[x][1])(i) for i in L])
        #     min_total = min(min_total, cost)

        return min_total


if __name__ == "__main__":
    s = Solution()
    costs = [[10,20],[30,200],[400,50],[30,20]]
    # costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    # costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]

    print(s.twoCitySchedCost(costs))