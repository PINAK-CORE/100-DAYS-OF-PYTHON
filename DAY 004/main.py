# DAY 4 : ROCK PAPER SCISSORS

import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_mode = input("Are you Ready To Play Rock Paper Scissors ? [1] lets roll [2] nahh")


while(game_mode == '1'):
    
    com_choice = r.ran