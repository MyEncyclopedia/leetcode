# AC
# Runtime: 24 ms, faster than 94.50% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.7 MB, less than 83.64% of Python3 online submissions for Letter Combinations of a Phone Number.

from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        iter_dims = [mapping[i] for i in digits]

        result = []
        for lst in product(*iter_dims):
            result.append(''.join(lst))

        return result
