# BILL SPLITER / TIP CALCULATOR
import math

print("WELCOME TO TIP CALCULATOR !! ")

bill = float(input("What was total bill ? : $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? : "))

total_bill = bill + ((bill*tip)/100)

ppl = int(input("How many people to split the bill? : "))

split = math.floor(total_bill/ppl )

print(f"Each person should pay : ${split}")