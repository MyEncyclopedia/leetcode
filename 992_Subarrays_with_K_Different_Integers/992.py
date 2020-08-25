# AC
# Runtime: 620 ms, faster than 65.77%
# Memory Usage: 16.3 MB, less than 75.61%

from collections import defaultdict
from typing import List, Dict

class Solution:
    def remove_key(self, d: Dict[int, int], key):
        d[key] -= 1
        if d[key] == 0:
            d.pop(key)

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ret = 0

        l, r1, r2 = 0, 0, 0
        win1, win2 = defaultdict(int), defaultdict(int)

        win1[A[l]] += 1
        win2[A[l]] += 1
        for l in range(len(A)):
            if l > 0:
                self.remove_key(win1, A[l - 1])
                self.remove_key(win2, A[l - 1])
            while len(win1) < K:
                r1 += 1
                if r1 == len(A):
                    return ret
                win1[A[r1]] += 1
            # len(win1) just == K

            while len(win2) <= K and r2 < len(A):
                r2 += 1
                if r2 >= len(A):
                    break
                win2[A[r2]] += 1
            # len(win2) just == K+1 or K but in the end
            ret += r2 - r1
        return ret

if __name__ == "__main__":
    s = Solution()
    A = [2,1,2,1,2]
    print(s.subarraysWithKDistinct(A, 2))

