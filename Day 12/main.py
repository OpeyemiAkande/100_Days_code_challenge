# choosing a random number between 1 and 100
import random
chosen_number = random.randint(1, 100)
# print(chosen_number)

#Make function to set difficulty.

def set_difficulty():

    attempt_prompt = input("Choose your difficulty level ").lower()

    if attempt_prompt == 'hard':
        attempt = 5
    elif attempt_prompt == 'easy':
        attempt = 10
    else:
        print('You entered a wrong input ')
    return attempt

def guessing_game():
    attempt = set_difficulty()
    while attempt > 0:
        
        #Let the user guess a number
        guess = int(input("Guess the a number between 1 and 100 "))

        if guess == chosen_number:
            print('You guessed the right number, You won!')
        else:
            attempt -= 1
            if guess > chosen_number:
                print(f'Your guess is too high, {attempt} attempts remaining')
            elif guess < chosen_number:
                print(f'Your guess is too low, {attempt} attempts remaining')
    else:
        print('You lost!')

# def checks_answer(guess, answer, attempts):
    

guessing_game()



            



#Function to check user's guess against actual answer.

#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.

