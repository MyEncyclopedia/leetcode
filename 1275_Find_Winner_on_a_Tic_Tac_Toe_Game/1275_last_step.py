# AC
from typing import List

class Solution:
    def checkWin(self, r: int, c: int) -> bool:
        north = self.getConnectedNum(r, c, -1, 0)
        south = self.getConnectedNum(r, c, 1, 0)

        east = self.getConnectedNum(r, c, 0, 1)
        west = self.getConnectedNum(r, c, 0, -1)

        south_east = self.getConnectedNum(r, c, 1, 1)
        north_west = self.getConnectedNum(r, c, -1, -1)

        north_east = self.getConnectedNum(r, c, -1, 1)
        south_west = self.getConnectedNum(r, c, 1, -1)

        if (north + south + 1 >= 3) or (east + west + 1 >= 3) or \
                (south_east + north_west + 1 >= 3) or (north_east + south_west + 1 >= 3):
            return True
        return False

    def getConnectedNum(self, r: int, c: int, dr: int, dc: int) -> int:
        player = self.board[r][c]
        result = 0
        i = 1
        while True:
            new_r = r + dr * i
            new_c = c + dc * i
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                if self.board[new_r][new_c] == player:
                    result += 1
                else:
                    break
            else:
                break
            i += 1
        return result

    def tictactoe(self, moves: List[List[int]]) -> str:
        self.board = [[0] * 3 for _ in range(3)]
        for idx, xy in enumerate(moves):
            player = 1 if idx % 2 == 0 else -1
            self.board[xy[0]][xy[1]] = player

        # only check last move
        r, c = moves[-1]
        win = self.checkWin(r, c)
        if win:
            return "A" if len(moves) % 2 == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"



