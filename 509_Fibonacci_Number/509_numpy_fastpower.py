# AC
# Runtime: 256 ms, faster than 26.21% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 29.4 MB, less than 5.25% of Python3 online submissions for Fibonacci Number.

class Solution:

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        import numpy as np
        F = np.array([[1, 1], [1, 0]])

        N -= 1
        powerDouble = F
        powers = np.array([[1, 0], [0, 1]])
        while N > 0:
            if N % 2 == 1:
                powers = np.matmul(powers, powerDouble)
            powerDouble = np.matmul(powerDouble, powerDouble)
            N = N // 2

        return powers[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))


