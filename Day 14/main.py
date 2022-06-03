#This is a game: Higher or lower.

from game_data import data
from random import choice
from art import logo, vs


def fetch_data(data):
    """This is a function that fetches data a list container"""
    return choice(data)

def format_data(account):
    """This is a function that formats the celebrity data into a presentable format: name, description and country to the user"""
    name = account['name']
    description = account['description']
    country = account['country']

    return f'{name}, {description}, from {country}'


# print(format_data(account_a))

def check_answer(guess, followers_a, followers_b):
    """This function checks the user input against the correct answer"""

    if followers_b > followers_a:
        answer = 'b'
    else:
        answer = 'a'

    if guess == answer:
        return True
    else:
        return False

def account_switcher(followers_a, followers_b):
    """A function that switches the accounts when the user guesses the correct answer"""

    if followers_a > followers_b:
        return 'a'
    else:
        return 'b'



def play_game():

    account_a = fetch_data(data)
    account_b = fetch_data(data)
    is_game_over = False
    score = 0

    while account_b == account_a:
        account_b = fetch_data(data)


    # print(check_answer(guess, followers_a, followers_b))

    while not is_game_over:
        print(logo)
        print(f'Compare A - {format_data(account_a)}')
        print(vs)
        print(f'Compare B - {format_data(account_b)}')
        followers_a = account_a['follower_count']
        followers_b = account_b['follower_count']
        guess = input('Who has more followers? Type A or B ').lower()

        if guess == '':
            print('You have not entered and option')

        if check_answer(guess, followers_a, followers_b):
            if account_switcher(followers_a, followers_b) == 'a':
                account_b = fetch_data(data)
            else:
                account_a = account_b
                account_b = fetch_data(data)
            score += 1



        else:
            is_game_over = True
            print('That was wrong!')
        print(f'Your score is {score}')
    response = input('Do you want to play again? Enter "y" or "n"').lower()
    while response == 'y':
        play_game()
    else:
        print('Okay, Bye')




play_game()











#     celeb_2 = []
# for item in celeb_dict_1, celeb_dict_2:
#     for key in item:
#         celeb_1.append(item[key])







