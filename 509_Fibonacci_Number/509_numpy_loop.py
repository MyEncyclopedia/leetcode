# AC
# Runtime: 92 ms, faster than 26.33% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 29.4 MB, less than 5.25% of Python3 online submissions for Fibonacci Number.

class Solution:

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        import numpy as np
        F = np.array([[1, 1], [1, 0]])
        P = F

        while N > 2:
            P = np.matmul(P, F)
            N -= 1

        return P[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))


