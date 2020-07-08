# AC
from typing import List

class Solution:

    def convertCell(self, c:str):
        return 1 if c == 'X' else -1 if c == 'O' else 0

    def validTicTacToe(self, board: List[str]) -> bool:
        turn = 0
        row, col = [0, 0, 0], [0, 0, 0]
        diag1, diag2 = False, False
        for r in range(3):
            for c in range(3):
                turn += self.convertCell(board[r][c])
                row[r] += self.convertCell(board[r][c])
                col[c] += self.convertCell(board[r][c])
                if r == c:
                    diag1 += self.convertCell(board[r][c])
                if r + c == 2:
                    diag2 += self.convertCell(board[r][c])

        xWin = any(row[r] == 3 for r in range(3)) or any(col[c] == 3 for c in range(3)) or diag1 == 3 or diag2 == 3
        oWin = any(row[r] == -3 for r in range(3)) or any(col[c] == -3 for c in range(3)) or diag1 == -3 or diag2 == -3
        if (xWin and turn == 0) or (oWin and turn == 1):
            return False
        return (turn == 0 or turn == 1) and (not xWin or not oWin)


if __name__ == "__main__":
    # board = ["O  ", "   ", "   "]
    board = ["XXX","OOX","OOX"]
    s = Solution()
    print(s.validTicTacToe(board))