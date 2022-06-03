import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#
# print(user_cards)
# print(computer_cards)

def compute_scores(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

# print(compute_scores(user_cards))

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif user_score == 0:
        return 'Blackjack! You win'
    elif computer_score == 0:
        return 'You lose, Opponent has a blackjack'
    elif user_score > 21:
        return 'You went over, opponent wins'
    elif computer_score > 21:
        return 'You win, Opponent went over'
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'You lose'

def play_game():
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    is_game_over = False
    while not is_game_over:
        computer_score = compute_scores(computer_cards)
        user_score = compute_scores(user_cards)
        print(f"Your cards are {user_cards}, your score {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            response = input('Do you still want to deal another card? Enter "y" to deal and "n" to stand').lower()
            if response == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = compute_scores(computer_cards)
    print(f'Your final hand {user_cards}, your final score {user_score}')
    print(f"computer's final hand {computer_cards}, Computer's final score {computer_score}")
    print(compare_scores(user_score, computer_score))

while input("Do you want to play the game of blackjack? y or n").lower():
    play_game()

