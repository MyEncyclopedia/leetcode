# AC
# Runtime: 36 ms, faster than 98.88% of Python3 online submissions for Number of Ways to Paint N × 3 Grid.
# Memory Usage: 13.9 MB, less than 58.66% of Python3 online submissions for Number of Ways to Paint N × 3 Grid.

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp2, dp3 = 6, 6
        n -= 1
        while n > 0:
            dp2, dp3 = (dp2 * 3 + dp3 * 2) % MOD, (dp2 * 2 + dp3 * 2) % MOD
            n -= 1
        return (dp2 + dp3) % MOD
