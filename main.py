# Allows the player to submit a guess for a number between 1 and 100.

from art import logo
from replit import clear 
import random
def num_of_tries(difficulty):
  if difficulty=='easy':
    print("You've got 10 attempts to guess the number")
    return 10
  elif difficulty=='hard':
    print("You've got 5 attempts to guess the number")
    return 5
  else:
    print("Invalid Value")
    return 0
def play_game():
  print(logo)
  print("🌟 Welcome to the NUMBER GUESSING GAME 🧐\n \n ")
  print("I'm thinking of number between 1 and 100.🤔🤔🤔")
  random_number=random.choice(range(1,101))
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  attempts=num_of_tries(difficulty)
  game_stop=False
  while attempts>0 and game_stop==False:
    guess=int(input("Make a guess: "))
    attempts-=1
    if guess<random_number:
      print("Too low\nGuess Again!")
    elif guess>random_number:
      print("Too high\nGuess Again! ")
    else: 
      print(f"You Won!!🥳🥳🥳 ... the answer is {random_number} ")
      game_stop=True
      
    if attempts!=0 and game_stop==False:
      print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts==0 and game_stop==False:
      print("You ran out of guesses. you lose 😭")
      game_stop=True

  if input("wanna play again type 'y' or 'n' : ").lower()=='y':
    clear()
    play_game()

    
play_game()   
  
