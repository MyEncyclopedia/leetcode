from typing import List

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre_i = 0
        ret = 0
        for j in range(1, len(A)):
            ret = max(A[pre_i] + pre_i + A[j] - j, ret)
            if A[j] + j > A[pre_i] + pre_i:
                pre_i = j
        return ret

