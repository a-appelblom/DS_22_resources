from deck import Deck


# from lessons.lesson5.imports.deck import Deck


def main():
    deck = Deck()
    while len(deck.cards) > 0:
        card = deck.pull_card()
        print(card)
        input()


if __name__ == '__main__':
    main()
