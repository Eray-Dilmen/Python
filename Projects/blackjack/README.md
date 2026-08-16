# Command-Line Blackjack Game ♠️♥️♣️♦️

Welcome to the Python Command-Line Blackjack game! This project is a text-based implementation of the classic casino card game, designed with modularity and object-oriented programming principles.

## The Objective
The goal of Blackjack is simple: beat the dealer by getting a hand value as close to **21** as possible without going over.

## Card Values
*   **Number Cards (2-10):** Worth their face value.
*   **Face Cards (Jack, Queen, King):** Each worth **10** points.
*   **Aces:** Can be worth **11** or **1**, whichever is more beneficial to the hand. The system automatically adjusts the Ace's value to prevent a bust.

## Core Rules
*   **Bust:** If your hand total exceeds 21, you "bust" and immediately lose your bet, regardless of the dealer's hand.
*   **Dealer's Rule:** The dealer plays strictly by casino rules. They must continue to take cards ("Hit") until their total is **17 or higher**. The dealer has no free will to stand early.
*   **Push (Tie):** If you and the dealer end up with the same total, it is a tie. Your bet is returned to you.
*   **Winning:** You win if the dealer busts, or if your final score is higher than the dealer's score without exceeding 21.

## How to Play
1.  **Place Your Bet:** At the start of each round, you will be prompted to enter a bet amount. You start with a default balance of 100 chips.
2.  **Initial Deal:** Both you and the dealer are dealt two cards. One of the dealer's cards remains hidden.
3.  **Your Turn (Hit or Stand):**
    *   Type `h` to **Hit**: Receive another card to increase your total score.
    *   Type `s` to **Stand**: Keep your current total and end your turn.
4.  **Dealer's Turn:** Once you stand, the dealer reveals their hidden card and plays their hand automatically.
5.  **Result:** The game evaluates both hands, distributes the chips accordingly, and asks if you would like to play another round.

## Project Structure
The codebase is divided into two main files to keep the logic clean and maintainable:
*   `modules.py`: Contains the core game mechanics, including the `Card`, `Deck`, `Hand`, and `Chips` classes, along with helper functions for game state evaluation.
*   `main.py`: The entry point of the game that imports the modules and handles the main execution loop and user interaction.

## Running the Game
To play the game, ensure you have Python installed on your system. Navigate to the project directory in your terminal and run the following command:

`python main.py`

## Developer Notes: Why `import modules`?

In `main.py`, you might notice that we import the entire module (`import modules`) in addition to specific classes and functions. 

This is specifically required to track the dynamic global state of the `playing` variable. If we had imported it using `from modules import playing`, Python would have only brought over a copy of its initial value (`True`). When the game ends in `modules.py` and `playing = False` is executed, `main.py` would not notice this change, causing an infinite loop. By using `import modules` and referencing `modules.playing`, we ensure the main loop points directly to the source reference rather than a static copy.