#DAY 7 HANGMEN
import random
temp = ["apple" , "banana" , "mango" , "kiwi"]

word = random.choice(temp)


guess = []
for i in range(len(word)):
    guess.append("_")

game_mode = True
while(game_mode):

    user_guess = input("Guess the Word > ")
    

print(word)
print(guess)
