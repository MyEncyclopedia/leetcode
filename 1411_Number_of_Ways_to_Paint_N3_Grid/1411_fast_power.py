# AC
# Runtime: 88 ms, faster than 39.07% of Python3 online submissions for Number of Ways to Paint N × 3 Grid.
# Memory Usage: 30.2 MB, less than 11.59% of Python3 online submissions for Number of Ways to Paint N × 3 Grid.

class Solution:
    def numOfWays(self, n: int) -> int:
        import numpy as np

        MOD = int(1e9 + 7)
        ret = np.array([[6, 6]])
        m = np.array([[3, 2], [2, 2]])

        n -= 1
        while n > 0:
            if n % 2 == 1:
                ret = np.matmul(ret, m) % MOD
            m = np.matmul(m, m) % MOD
            n = n // 2
        return int((ret[0][0] + ret[0][1]) % MOD)