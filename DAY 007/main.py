#DAY 7 HANGMEN
import random
temp = ["apple" , "banana" , "mango" , "kiwi"]

word = random.choice(temp)


guess = []
for i in range(len(word)):
    guess.append("_")


print(word)
print(guess)
