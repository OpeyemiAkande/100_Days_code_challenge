
import random
from Hangman_art import stages, logo
from Hangman_wordlist import word_list

print(logo)
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
  display.append('_')
print(display)

# This block of code implements the game rules
life = 6
while life > 0:

  guess = input("Guess a letter: ").lower()


  # This block of code checks every letter in the chosen word matches the guessed letter sets it at the correct position in display.
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  
  #This block punishes the user for wrong guesses
  if guess not in chosen_word:
    print(stages[life])
    print(f'Your guess is wrong, You have {life-1} lives remaining')
  
    life -= 1
  
  print(display)
  
  #This block checks the conditions for losing or winning the game
  if display == list(chosen_word):
    print('You won, Game Over')
    life = 0
  
  elif life == 0:
    print(stages[life])
    print(f'You lost, the correct word is {chosen_word} Game Over')