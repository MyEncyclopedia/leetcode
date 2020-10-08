# AC
# Runtime: 96 ms, faster than 81.18% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14.2 MB, less than 13.53% of Python3 online submissions for Champagne Tower.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        N = 100
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i+1][j] += (dp[i][j] - 1) / 2.0
                    dp[i+1][j + 1] += (dp[i][j] - 1) / 2.0
        return min(1, dp[query_row][query_glass])
