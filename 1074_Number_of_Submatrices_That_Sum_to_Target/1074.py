# AC
# Runtime: 6476 ms, faster than 70.93% of Python3
# Memory Usage: 20.9 MB, less than 48.94% of Python3
# Time complexity O(R*R*C)
# Space complexity: O(C)

from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ret = 0
        X = len(matrix)
        Y = len(matrix[0])
        for x1 in range(0, X):
            prevRows = {}
            for x2 in range(x1, X):
                thisRow = {}
                preSumDict = {0: 1} # value => occurrence
                preSum = 0
                for y in range(Y):
                    colSum = prevRows.get(y, 0) + matrix[x2][y]
                    thisRow[y] = colSum
                    preSum += colSum
                    complement = preSum - target
                    ret += preSumDict.get(complement, 0)
                    preSumDict[preSum] = preSumDict.get(preSum, 0) + 1
                prevRows = thisRow
        return ret


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, -1], [-1, 1]]
    print(s.numSubmatrixSumTarget(matrix, 0))

