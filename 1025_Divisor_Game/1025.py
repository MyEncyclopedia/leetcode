import math
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N+1)
        dp[1] = False
        for i in range(2, N+1):
            for m in range(1, int(math.sqrt(i)) + 1):
                if i % m == 0 and not dp[i-m]:
                    dp[i] = True
                    break
        
        return dp[N]

if __name__ == "__main__":
    s = Solution()
    print(s.divisorGame(3))