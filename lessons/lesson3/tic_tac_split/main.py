from game import Game


def main():
    game = Game()
    game.start_game()

    game.print_board()
    game.print_winner()


main()
