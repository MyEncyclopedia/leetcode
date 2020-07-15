# AC
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        remainders = set([1])
        r = 1
        for len in range(2, K+1):
            r = (10 * r + 1) % K
            if r == 0:
                return len
            if r in remainders:
                return -1
            else:
                remainders.add(r)
        
        return -1
