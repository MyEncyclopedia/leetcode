# AC
# Runtime: 1416 ms, faster than 46.67%
# Memory Usage: 14.6 MB, less than 72.59%
import copy
from collections import defaultdict
from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for v in rods:
            dp_ = copy.deepcopy(dp)
            for diff, max_v in dp.items():
                dp_[diff + v] = max(dp_[diff+v], dp[diff])
                dp_[abs(diff - v)] = max(dp_[abs(diff-v)], max_v + min(diff,v))
            dp = dp_
        return dp[0]
