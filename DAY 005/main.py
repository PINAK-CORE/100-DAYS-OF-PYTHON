# DAY 5 : Passworld Genrator

import random as r


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_letters = int(input(" HOW MANY NO. OF LETTERS YOU WANTS > "))

no_number = int(input(" HOW MANY numbers YOU WANTS > "))

no_symbols = int(input(" HOW MANY NO. OF SYMBOLS YOU WANTS > "))

password = ""

for char in range(1, no_letters + 1):
  password += r.choice(letters)

for char in range(1, no_symbols + 1):
  password += r.choice(symbols)

for char in range(1, no_number + 1):
  password += r.choice(numbers)


l= list(password)
r.shuffle(l)

password = "".join(l)

print(password)