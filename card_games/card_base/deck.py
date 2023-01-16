from typing import List
from card import Card, CardSuit, CardValue


print(__name__)


class Deck:
    cards: List[Card] = []

    def __init__(self):
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(value, suit))
        # for card in self.cards:
        #     print(card)

    def pull_card(self):
        return self.cards.pop()
