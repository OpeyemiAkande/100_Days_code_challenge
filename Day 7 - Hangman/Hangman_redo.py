import random
from Hangman_art import stages, logo
from Hangman_wordlist import word_list

print(logo)

chosen_word = random.choice(word_list)

# print(f'The chosen word is {chosen_word}')

display = []
for position in range(len(chosen_word)):
    display += '_'

print(display)

life = 6

# This block of code implements the game rules
while life > 0:

    #prompts player for an input
    guess = input('Guess a letter of the unkown word above: ').lower()
    
    #checks every letter of the chosen word  and compares it with the guess above
    for position in range(len(chosen_word)):
        
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
    
    print(display)

    #punishes the player for each letter wrongly guessed
    if guess not in chosen_word:
        print(stages[life])
        life -= 1
        print(f'You guessed a wrong letter. You have {life} life remaining')
        

    #checks if the condition for winning or loosing have been fulfilled
    if display == list(chosen_word):
        life = 0
        print('You won, game over')
    elif life == 0:
        print(stages[life])
        print('You lost, game over')


        

    # print(life)

print(display)
        
