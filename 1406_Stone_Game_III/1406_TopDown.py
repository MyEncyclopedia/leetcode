# 7948 ms, faster than 5.22%
import math
from functools import lru_cache
from typing import List

class Solution:

    @lru_cache(maxsize=None)
    def maxDiff(self, l: int, r: int) -> int:
        if l > r:
            return 0
        ret = -math.inf
        for i in range(l, l + 3):
            if i > r:
                break
            ret = max(ret, sum(self.stoneValue[l:i+1]) - self.maxDiff(i + 1, r))
        return ret

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.stoneValue = stoneValue
        result = self.maxDiff(0, len(stoneValue) - 1)
        if result > 0:
            return 'Alice'
        elif result < 0:
            return 'Bob'
        else:
            return 'Tie'

if __name__ == "__main__":
    nums = [1,2,3,7]
    print(Solution().stoneGameIII(nums))