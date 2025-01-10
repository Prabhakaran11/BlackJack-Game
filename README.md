# BlackJack-Game
A command-line Blackjack game implemented in Python, automated dealer gameplay, and classic casino rules. Perfect for learning Python while having fun! 🎰

# Python Blackjack Game 🎰
A command-line implementation of the classic casino card game Blackjack (also known as 21). This project features a simple yet engaging interface where players can compete against a computer dealer following standard Blackjack rules.

## Features
- Text-based user interface with ASCII art logo
- Standard Blackjack gameplay mechanics
- Automated dealer (computer) decisions
- Ace value handling (11 or 1)
- Blackjack (21) detection
- Continuous play option

## Requirements

- Python 3.6 or higher
- `art` package for ASCII art

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-blackjack.git
cd python-blackjack
```

## How to Play

1. Run the game:
```bash
python blackjack.py
```

2. Follow the on-screen prompts:
   - Type 'y' to start a new game
   - During the game, type 'y' to hit (get another card) or 'n' to stand
   - Try to get as close to 21 as possible without going over
   - Beat the dealer's hand to win!

## Game Rules

- The goal is to get a hand value closer to 21 than the dealer without going over
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10
- Aces are worth 11 but change to 1 if the hand would bust
- The dealer must hit on 16 and stand on 17
- Getting 21 with your first two cards is a Blackjack!

## Code Structure

- `draw_card()`: Randomly selects a card from the deck
- `start_game()`: Initializes the game by dealing two cards each
- `calculate_ace_value()`: Handles the dynamic value of aces
- `display_score()`: Shows the current or final game state
- `play_game()`: Main game logic and flow control

## Author

Prabhakaran Srinivasan

## Acknowledgments

- Built as a Python learning project
