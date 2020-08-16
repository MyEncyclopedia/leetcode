# AC: 2544 ms, faster than 5.08%

import math
from typing import List

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        dec_stack = []  # value is index of A
        for i, v in enumerate(A):
            if len(dec_stack) == 0 or (len(dec_stack) > 0 and v < A[dec_stack[-1]]):
                dec_stack.append(i)
        max_r = -math.inf
        max_width = 0
        for r in range(len(A)-1, -1, -1):
            n = A[r]
            if n < max_r:
                continue
            max_r = n
            while len(dec_stack) > 0:
                # pop top <= n
                left_idx = dec_stack[-1]
                if A[left_idx] <= n:
                    dec_stack = dec_stack[0:-1]
                    max_width = max(max_width, r - left_idx)
                else:
                    break
            if len(dec_stack) == 0:
                break
        return max_width


if __name__ == "__main__":
    s = Solution()
    A = [9,8,1,0,1,9,4,0,4,1]
    # A = [6,0,8,2,1,5]
    print(s.maxWidthRamp(A))




