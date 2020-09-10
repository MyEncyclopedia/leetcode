# AC
# Runtime: 84 ms, faster than 95.43% of Python3 online submissions for Combinations.
# Memory Usage: 15.2 MB, less than 68.98% of Python3 online submissions for Combinations.
from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [c for c in combinations(list(range(1, n + 1)), k)]


