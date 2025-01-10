import random

import art

# Method to draw the card from the list of cards
def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Method to initialise the game and assign two cards for each player and the computer
def start_game():
    return [draw_card() for _ in range(2)]

# Method to calculate the ace value.
def calculate_ace_value(card_list):
    while sum(card_list) > 21 and 11 in card_list:
        index = card_list.index(11)
        card_list[index] = 1
    return card_list

# Method to determine whether to display current score or final score
def display_score(player_card, computer_card, end_game=False):
    if end_game:
        print(f"  Your final hand: {player_card}, final score: {sum(player_card)}")
        print(f"  Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
    else:
        print(f"    Your cards: {player_card}, current score: {sum(player_card)}")
        print(f"    Computer's first card: {computer_card[0]}")

# Method to play the game
def play_game():
    print("\n" * 50)
    print(art.logo)

    players_card = start_game()
    computers_card = start_game()
    game_over = False

    calculate_ace_value(players_card)
    calculate_ace_value(computers_card)

    #Checking for BlackJack
    if sum(computers_card) == 21:
        display_score(players_card, computers_card, end_game=True)
        print("Computer has Blackjack! You lose...")
        return
    elif sum(players_card) == 21:
        display_score(players_card, computers_card, end_game=True)
        print("Blackjack! You win...")
        return

    # Player's turn to play
    while not game_over:
        calculate_ace_value(players_card)
        display_score(players_card, computers_card)

        if sum(players_card) > 21:
            display_score(players_card, computers_card, end_game=True)
            print("You went over. You lose...")
            break

        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == 'y':
            players_card.append(draw_card())
        else:
            game_over = True

    # Computer's turn - calculate ace value after each draw
    while sum(computers_card) <= 16:
        computers_card.append(draw_card())
        calculate_ace_value(computers_card)

    # Final scoring
    player_score = sum(players_card)
    computer_score = sum(computers_card)

    display_score(players_card, computers_card, end_game=True)

    if player_score > 21:
        print("You went over. You lose...")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("You lose...")
    else:
        print("It's a draw!")

# Start the game
while True:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")
        break
