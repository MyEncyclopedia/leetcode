# AC
import math
from typing import List

class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue += [0, 0, 0]  # dummy
        dp = [-math.inf] * n + [0, 0, 0] # dummy
        for i in range(n-1, -1, -1):
            for k in (1, 2, 3):
                dp[i] = max(dp[i], sum(stoneValue[i:i+k]) - dp[i+k])

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"

if __name__ == "__main__":
    nums = [1,2,3,7]
    print(Solution().stoneGameIII(nums))
