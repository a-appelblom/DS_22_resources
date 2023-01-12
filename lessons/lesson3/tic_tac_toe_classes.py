from typing import List, Tuple
from enum import Enum


class Player(Enum):
    X = "X"
    O = "O"


class Round:
    board: List[List[int]]
    player: Player

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def run_round(self):
        row, col = self.get_input()
        self.update_board(row, col)
        pass

    def get_input(self) -> Tuple[int, int]:
        valid = False
        print(f"Det är spelare {self.player.value}s tur")
        while not valid:
            coordinates_string = input(
                "rad och kolumn för markering separera med mellanrum: ")
            valid, res = self.validate_input(coordinates_string)

        return res

    def validate_input(self, string: str) -> Tuple[bool, Tuple[int, int]]:
        string = string.strip()
        split_string: List[str] = string.split(" ")
        if len(split_string) < 2:
            print("Fel input")
            return (False, None)
        if not str.isdigit(split_string[0]) or not str.isdigit(split_string[1]):
            print("Fel input")
            return (False, None)

        row: int = int(split_string[0])
        col: int = int(split_string[1])
        # if row > 3 or col > 3 or row < 1 or col < 1:
        if not 1 <= row <= 3 or not 1 <= col <= 3:
            print("Fel input")
            return (False, None)

        if self.board[row - 1][col - 1] != "#":
            print("Fel input")
            return (False, None)

        return (True, (row - 1, col - 1))

    def update_board(self, row: int, col: int):
        self.board[row][col] = self.player.value


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


def main():
    game = Game()
    game.start_game()

    game.print_board()
    game.print_winner()


main()
