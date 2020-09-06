# AC
# Runtime: 156 ms, faster than 41.86% of Python3 online submissions for 24 Game.
# Memory Usage: 14 MB, less than 10.33% of Python3 online submissions for 24 Game.

import math
from itertools import permutations, product
from typing import List

class Solution:

    def eval_trees(self, op1, op2, op3, a, b, c, d):
        yield op1(op2(a, b), op3(c, d))
        yield op1(a, op2(op3(b, c), d))
        yield op1(op2(op3(a, b), c), d)
        yield op1(op2(op3(a, b), c), d)
        yield op1(a, op2(b, op3(c, d)))
        yield op1(op2(a, op3(b, c)), d)

    def judgePoint24(self, nums: List[int]) -> bool:
        mul = lambda x, y: x * y
        plus = lambda x, y: x + y
        div = lambda x, y: x / y if y != 0 else math.inf
        minus = lambda x, y: x - y

        op_lst = [plus, minus, mul, div]

        for ops in product(op_lst, repeat=3):
            for val in permutations(nums):
                for v in self.eval_trees(ops[0], ops[1], ops[2], val[0], val[1], val[2], val[3]):
                    if abs(v - 24) < 0.0001:
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([6, 1, 3, 4]))

