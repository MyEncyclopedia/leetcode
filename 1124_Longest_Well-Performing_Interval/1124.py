# AC
# Runtime: 320 ms, faster than 26.67%
# Memory Usage: 14.3 MB, less than 80.83%

import math
from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pre_sum = [0]
        for i, v in enumerate(hours):
            hours[i] = 1 if v > 8 else -1
            pre_sum.append(pre_sum[-1] + hours[i])

        dec_stack = [] # idx to pre_sum
        for i, v in enumerate(pre_sum):
            if len(dec_stack) == 0 or (len(dec_stack) > 0 and v < pre_sum[dec_stack[-1]]):
                dec_stack.append(i)
        max_r = -math.inf
        max_width = 0
        for r in range(len(pre_sum)-1, -1, -1):
            n = pre_sum[r]
            if n < max_r:
                continue
            max_r = n
            while len(dec_stack) > 0:
                # pop top < n
                left_idx = dec_stack[-1]
                if pre_sum[left_idx] < n:
                    dec_stack = dec_stack[0:-1]
                    max_width = max(max_width, r - left_idx)
                else:
                    break
            if len(dec_stack) == 0:
                break
        return max_width



if __name__ == "__main__":
    s = Solution()
    hours = [9, 9, 6, 0, 6, 6, 9]
    print(s.longestWPI(hours))

