"""
Blackjack Main Game Execution

This file imports the necessary logic from modules.py and
runs the main execution loop of the Blackjack game.
"""

from modules import (
    Deck, Hand, Chips, take_bet, show_some_cards, hit_or_stand, hit,
    show_all_cards, player_busts, dealer_busts, dealer_wins, player_wins, push
)
import modules  # Required to track the global 'playing' state (see README for details)


def main():
    print("Welcome to Blackjack!")

    # Initialize player chips once outside the main loop
    player_chips = Chips()

    while True:
        # 1. Setup the game: Create and shuffle deck
        deck = Deck()
        deck.shuffle()

        # 2. Deal initial two cards to player and dealer
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # 3. Take player's bet
        take_bet(player_chips)

        # 4. Show initial cards (one dealer card hidden)
        show_some_cards(player_hand, dealer_hand)

        # 5. Player's turn: Hit or Stand loop
        while modules.playing:
            hit_or_stand(deck, player_hand)

            if modules.playing:
                show_some_cards(player_hand, dealer_hand)

            # Check for player bust
            if player_hand.value > 21:
                show_all_cards(player_hand, dealer_hand)
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # 6. Dealer's turn (only if player hasn't busted)
        if player_hand.value <= 21:
            # Dealer must hit until they reach at least 17
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all_cards(player_hand, dealer_hand)

            # 7. Evaluate the final game state
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # 8. Display current chip balance
        print(f"\nPlayer chips total: {player_chips.total}")

        # 9. End game if player is out of chips
        if player_chips.total <= 0:
            print("You are out of chips! Game over.")
            break

        # 10. Ask to play again and handle input validation
        while True:
            new_game = input("Would you like to play again? Enter 'y' or 'n': ")
            if new_game and new_game[0].lower() in ['y', 'n']:
                break
            print("Invalid input! Please enter 'y' or 'n'.")

        if new_game[0].lower() == 'y':
            modules.playing = True
            continue
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()