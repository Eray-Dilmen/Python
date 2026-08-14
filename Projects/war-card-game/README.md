# 🃏 War Card Game Simulation

A Python implementation of the classic "War" card game. This project is built as an automated simulation to demonstrate fundamental Object-Oriented Programming (OOP) concepts in Python.

## 📌 Project Overview
Unlike interactive games, this script runs completely autonomously. The computer shuffles a standard 52-card deck, distributes it equally between two virtual players, and plays out the entire game until one player runs out of cards. 

It highlights the use of:
*   **Object-Oriented Programming:** Modular design using `Card`, `Deck`, and `Player` classes.
*   **State Management:** Tracking the deck, player hands, and the cards on the table.
*   **Logic & Loops:** Resolving normal rounds and handling edge cases like recursive "War" scenarios when card values tie.

## ⚙️ How It Works
1.  A deck of 52 unique cards is generated and shuffled.
2.  Cards are dealt evenly to Player One and Player Two (26 cards each).
3.  In each round, both players reveal their top card.
    *   The player with the higher card value takes both cards and adds them to the bottom of their deck.
    *   If the values are equal, a **WAR** is declared. Both players draw 5 additional cards, and the last cards are compared to determine the winner of the pot.
4.  The game automatically loops until one player has 0 cards left.

## 🚀 How to Run
To run the simulation and watch the rounds unfold in your terminal:

```bash
python main.py
```

## 📁 File Structure

*   `models.py`: Contains the core classes (`Card`, `Deck`, `Player`) and global constraints.
*   `main.py`: Contains the game setup and the main execution loop.
