# AC
# Runtime: 180 ms, faster than 45.36% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.6 MB, less than 14.23% of Python3 online submissions for Interval List Intersections.
from enum import Enum
from typing import List, Tuple

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ret = []
        lines: List[Tuple] = []
        for interval in A:
            lines.append((interval[0], 0, 'A'))
            lines.append((interval[1], 1, 'A'))
        for interval in B:
            lines.append((interval[0], 0, 'B'))
            lines.append((interval[1], 1, 'B'))
        lines.sort()

        class State(Enum):
            EMPTY = 0
            SINGLE = 1
            SEGMENT = 2

        s = State.EMPTY
        for line in lines:
            if s == State.EMPTY:
                s = State.SINGLE
            elif s == State.SINGLE:
                if line[1] == 0:
                    seg_start = line[0]
                    s = State.SEGMENT
                else:
                    s = State.EMPTY
            elif s == State.SEGMENT:
                s = State.SINGLE
                ret.append([seg_start, line[0]])
        return ret


if __name__ == '__main__':
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    s = Solution()
    print(s.intervalIntersection(A, B))
