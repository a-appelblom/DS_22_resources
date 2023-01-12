from typing import List, Tuple
from player import Player


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
