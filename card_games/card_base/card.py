# card

from dataclasses import dataclass
from enum import Enum


class CardValue(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    KNIGHT = "Knight"
    QUEEN = "Queen"
    KING = "King"


class CardSuit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    SPADES = "♠"
    CLUBS = "♣"


print(__name__)


@dataclass
class Card:
    suit: CardSuit
    value: CardValue

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.suit.value} {self.value.value}"
