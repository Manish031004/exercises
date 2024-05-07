from player import Player
from board import Board


class Game:
    def __init__(self):
        print("Welcome to cConnect 4")

        p1 = Player("barrie", "x")
        p2 = Player("barbie", "0")

        board = board(7, 6)
        board.print_board()

        won = False
        while not won:
            active_player = p1

            selection = input(f"{active_player.name}, please select your name")
            if not selection.isnumeric():
                print("wrong selection, must be a number")
                continue

            column = int(selection) - 1
            if not board.is_valid_column(column):
                print("please a valid one")
                continue

            row = board.check_column(column)
            if row == -1:
                print("row full")
                continue

            board.add_token(column, row, active_player.token)
            board.print_board()


game = Game()
