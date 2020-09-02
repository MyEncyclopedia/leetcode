from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ret = self.totalLessEq(A, K)
        if K > 1:
            ret -= self.totalLessEq(A, K-1)
        return ret

    def totalLessEq(self, A: List[int], K: int) -> int:
        c2n_map = {}
        ret = 0
        i_start = 0
        i_end = -1
        while True:
            # try i_end, until sliding window > K
            while len(c2n_map) <= K and i_end + 1 < len(A):
                char = A[i_end + 1]
                if char in c2n_map or len(c2n_map) < K:
                    i_end += 1
                    c2n_map.setdefault(char, 0)
                    c2n_map[char] += 1
                else:
                    break
            if i_end == len(A) - 1:
                break

            # inc i_start and count
            while len(c2n_map) == K:
                ret += i_end - i_start + 1
                char = A[i_start]
                c2n_map[char] -= 1
                if c2n_map[char] == 0:
                    c2n_map.pop(char)
                i_start += 1

        for i in range(i_start, i_end + 1):
            ret += i_end - i + 1

        return ret