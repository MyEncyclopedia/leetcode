# AC
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        for idx, xy in enumerate(moves):
            player = 1 if idx % 2 == 0 else -1
            board[xy[0]][xy[1]] = player

        turn = 0
        row, col = [0, 0, 0], [0, 0, 0]
        diag1, diag2 = False, False
        for r in range(3):
            for c in range(3):
                turn += board[r][c]
                row[r] += board[r][c]
                col[c] += board[r][c]
                if r == c:
                    diag1 += board[r][c]
                if r + c == 2:
                    diag2 += board[r][c]

        oWin = any(row[r] == 3 for r in range(3)) or any(col[c] == 3 for c in range(3)) or diag1 == 3 or diag2 == 3
        xWin = any(row[r] == -3 for r in range(3)) or any(col[c] == -3 for c in range(3)) or diag1 == -3 or diag2 == -3

        return "A" if oWin else "B" if xWin else "Draw" if len(moves) == 9 else "Pending"



