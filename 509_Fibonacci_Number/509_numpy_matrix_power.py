# AC
# Runtime: 116 ms, faster than 26.25% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 29.2 MB, less than 5.25% of Python3 online submissions for Fibonacci Number.

class Solution:

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        from numpy.linalg import matrix_power
        import numpy as np
        F = np.array([[1, 1], [1, 0]])
        F = matrix_power(F, N - 1)

        return F[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.fib(2))


