from typing import List

from player import Player
from round import Round


class Game:
    board: List[List[str]] = [['#', '#', '#'],
                              ['#', '#', '#'],
                              ['#', '#', '#']]
    active_player: Player = Player.O
    winner: Player | None = None
    active_round: int = 0

    def start_game(self):
        while not self.winner:
            self.print_board()
            self.active_round += 1
            Round(self.board, self.active_player).run_round()
            has_winner = self.check_for_win()
            if has_winner:
                self.winner = self.active_player
            self.toggle_player()

    def toggle_player(self):
        self.active_player = Player.O if self.active_player == Player.X else Player.X
        pass

    def print_winner(self):
        print(f"Vinnaren är {self.winner. value}, Hurra Hurra Hurra")
        pass

    def print_board(self):
        print("")
        for row in self.board:
            print(row)
        print("")

    def check_for_win(self):
        board = self.board
        # Kolla rader
        for row in board:
            row_set = set(row)
            if len(row_set) == 1 and row_set.pop() != "#":
                return True

        # Kolla kolumner
        for i in range(2):
            col_set = {board[0][i], board[1][i], board[2][i]}
            if len(col_set) == 1 and col_set.pop() != "#":
                return True

        # Kolla diagonaler
        across_set1 = {board[0][0], board[1][1], board[2][2]}
        if len(across_set1) == 1 and across_set1.pop() != "#":
            return True
        across_set2 = {board[0][2], board[1][1], board[2][0]}
        if len(across_set2) == 1 and across_set2.pop() != "#":
            return True

        return False
