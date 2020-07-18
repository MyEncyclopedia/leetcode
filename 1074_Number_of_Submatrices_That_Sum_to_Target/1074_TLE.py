# TLE
# Time complexity O(M*M*N*N)
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ret = 0
        X = len(matrix)
        Y = len(matrix[0])
        dp = {}
        for xLen in range(1, X+1):
            for yLen in range(1, Y+1):
                for x1 in range(X):
                    for y1 in range(Y):
                        x2 = x1 + xLen - 1
                        y2 = y1 + yLen - 1
                        if x2 >= X or y2 >= Y:
                            continue
                        upperLeft = dp.get((x1, y1, x2-1, y2-1), 0)
                        right = dp.get((x1, y2, x2-1, y2), 0)
                        bottom = dp.get((x2, y1, x2, y2-1), 0)
                        area = upperLeft + right + bottom + matrix[x2][y2]
                        if area == target:
                            ret += 1
                        dp[(x1, y1, x2, y2)] = area
        return ret


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, -1], [-1, 1]]
    print(s.numSubmatrixSumTarget(matrix, 0))

