"""
Blackjack Modules

This file contains the core classes and helper functions required
to run the Blackjack game. It handles the logic for cards, decks,
hands, betting chips, and game state evaluations.
"""

import random

# Global Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace'
)
VALUES = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
    'Ace': 11
}

# Global variable to control the game loop
playing = True


class Card:
    """Represents a single playing card."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a standard 52-card deck."""

    def __init__(self):
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffles the deck randomly."""
        random.shuffle(self.all_cards)

    def deal(self):
        """Removes and returns a single card from the deck."""
        return self.all_cards.pop()


class Hand:
    """Represents the cards held by the player or the dealer."""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """Adds a card to the hand and updates the total value."""
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        """Adjusts the value of an Ace from 11 to 1 if the hand exceeds 21."""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """Tracks the player's starting balance and current bets."""

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        return f"Total: {self.total}"


def take_bet(chips):
    """Prompts the player to enter a valid bet amount."""
    while True:
        try:
            chips.bet = int(input('Enter amount of money you will play: '))
        except ValueError:
            print("You must enter an integer amount, please try again")
        else:
            if chips.bet > chips.total:
                print(f"You can't bet {chips.bet}. You have a maximum of {chips.total}. Please try again.")
            elif chips.bet <= 0:
                print("You entered a negative or zero amount, please enter a positive amount.")
            else:
                break


def hit(deck, hand):
    """Deals a card to the specified hand and adjusts for Aces."""
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """Prompts the player to Hit or Stand."""
    global playing

    while True:
        x = input("\nHit or Stand? Enter h or s: ")
        if not x:
            continue

        if x[0].lower() == 'h':
            print("--------------------------")
            print("Player Hits!")
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("--------------------------")
            print("Player Stands.")
            playing = False
        else:
            print("Sorry, you have to enter h or s. Please try again.")
            continue
        break


def show_some_cards(player, dealer):
    """Displays the player's full hand and one of the dealer's cards."""
    print("--------------------------")
    print("\nDealer's Hand:\n")
    print("First Card Is Hidden")
    print(dealer.cards[1])

    print("\n\nPlayer's Hand:\n")
    for card in player.cards:
        print(card)


def show_all_cards(player, dealer):
    """Displays all cards and total values for both the player and the dealer."""
    print("--------------------------")
    print("\nDealer's Hand:\n")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\n\nPlayer's Hand:\n")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("--------------------------")
    print(f"\nPLAYER BUSTED! Your score: {player.value} (exceeded 21). Lost bet: {chips.bet}")
    print("--------------------------")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("--------------------------")
    print(f"\nPLAYER WINS! Your score: {player.value} > Dealer: {dealer.value}. Won bet: {chips.bet}")
    print("--------------------------")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("--------------------------")
    print(f"\nPLAYER WINS! Dealer busted with {dealer.value}. Won bet: {chips.bet}")
    print("--------------------------")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("--------------------------")
    print(f"\nDEALER WINS! Dealer: {dealer.value} > Your score: {player.value}. Lost bet: {chips.bet}")
    print("--------------------------")
    chips.lose_bet()


def push(player, dealer):
    print("--------------------------")
    print(f"\nPUSH! It is a tie. (Player: {player.value} | Dealer: {dealer.value})")
    print("--------------------------")