# AC
# Runtime: 112 ms, faster than 57.59% of Python3 online submissions for 24 Game.
# Memory Usage: 13.7 MB, less than 85.60% of Python3 online submissions for 24 Game.

import math
from itertools import permutations, product
from typing import List

class Solution:

    def iter_trees(self, op1, op2, op3, a, b, c, d):
        yield op1(op2(a, b), op3(c, d))
        yield op1(a, op2(op3(b, c), d))
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
                for v in self.iter_trees(ops[0], ops[1], ops[2], val[0], val[1], val[2], val[3]):
                    if abs(v - 24) < 0.0001:
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([3, 3, 7, 7]))

