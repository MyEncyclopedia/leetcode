# AC
# Runtime: 32 ms, faster than 54.28% of Python3 online submissions for Pow(x, n).
# Memory Usage: 14.2 MB, less than 5.04% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1.0
        i = abs(n)
        while i != 0:
            if i & 1:
                ret *= x
            x *= x
            i = i >> 1
        return 1.0 / ret if n < 0 else ret

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.0, -5))



