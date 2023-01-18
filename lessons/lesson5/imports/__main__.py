from card_game_base.deck import Deck
from classes import Dog
# from lesson5.classes import Dog


# from lessons.lesson5.imports.deck import Deck


def main():
    deck = Deck()
    while len(deck.cards) > 0:
        card = deck.pull_card()
        print(card)
        input()


if __name__ == '__main__':
    main()
