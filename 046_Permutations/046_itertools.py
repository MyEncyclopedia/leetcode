# AC
# Runtime: 36 ms, faster than 91.78% of Python3 online submissions for Permutations.
# Memory Usage: 13.9 MB, less than 66.52% of Python3 online submissions for Permutations.

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [p for p in permutations(nums)]

