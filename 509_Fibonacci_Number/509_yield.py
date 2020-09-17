# AC
# Runtime: 28 ms, faster than 85.56% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 58.41% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        i = 2
        for fib in self.fib_next():
            if i == N:
                return fib
            i += 1

    def fib_next(self):
        f_last2, f_last = 0, 1
        while True:
            f = f_last2 + f_last
            f_last2, f_last = f_last, f
            yield f
