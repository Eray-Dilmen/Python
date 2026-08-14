import random

# Global Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """Represents a single playing card with a suit, rank, and integer value."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Generates and manages a standard 52-card deck."""

    def __init__(self):
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffles the deck in-place."""
        random.shuffle(self.all_cards)

    def distribute_card(self):
        """Removes and returns a single card from the top of the deck."""
        return self.all_cards.pop()


class Player:
    """Represents a player with a hand of cards."""

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def player_put_to_table(self):
        """Removes and returns the top card from the player's hand."""
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        """Adds one or multiple cards to the bottom of the player's hand."""
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."