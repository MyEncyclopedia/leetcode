# AC 9184 ms, faster than 28.44% Python3
# Time complexity O(Row*Row*Col)
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ret = 0
        X = len(matrix)
        Y = len(matrix[0])
        for x1 in range(0, X):
            dp = {}  # x2, y => int
            for x2 in range(x1, X):
                preSumDict = {0: 1} # value => occurrence
                preSum = 0
                for y in range(Y):
                    colSum = dp.get((x2-1, y), 0) + matrix[x2][y]
                    dp[(x2, y)] = colSum
                    preSum += colSum
                    complement = preSum - target
                    ret += preSumDict.get(complement, 0)
                    preSumDict[preSum] = preSumDict.get(preSum, 0) + 1
        return ret


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, -1], [-1, 1]]
    print(s.numSubmatrixSumTarget(matrix, 0))

