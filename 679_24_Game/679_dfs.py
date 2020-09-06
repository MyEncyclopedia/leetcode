# AC
# Runtime: 116 ms, faster than 56.23% of Python3 online submissions for 24 Game.
# Memory Usage: 13.9 MB, less than 44.89% of Python3 online submissions for 24 Game.

import math
from itertools import combinations, product, permutations
from typing import List

class Solution:

    def judgePoint24(self, nums: List[int]) -> bool:
        mul = lambda x, y: x * y
        plus = lambda x, y: x + y
        div = lambda x, y: x / y if y != 0 else math.inf
        minus = lambda x, y: x - y

        op_lst = [plus, minus, mul, div]

        def recurse(lst: List[int]):
            if len(lst) == 2:
                for op, values in product(op_lst, permutations(lst)):
                    yield op(values[0], values[1])
            else:
                for choosen_idx_lst in combinations(list(range(len(lst))), 2):
                    idx_remaining_set = set(list(range(len(lst)))) - set(choosen_idx_lst)
                    value_remaining_lst = list(map(lambda x: lst[x], idx_remaining_set))
                    for op, idx_lst in product(op_lst, permutations(choosen_idx_lst)):
                        value_remaining_lst.append(op(lst[idx_lst[0]], lst[idx_lst[1]]))
                        yield from recurse(value_remaining_lst)
                        value_remaining_lst = value_remaining_lst[:-1]

        for v in recurse(nums):
            if abs(v - 24) < 0.0001:
                return True


if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([6, 1, 3, 4]))

