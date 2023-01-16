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


@dataclass
class Card:
    suit: CardSuit
    value: CardValue
