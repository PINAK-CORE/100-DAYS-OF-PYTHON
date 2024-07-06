#FUNCTION

#creating a function
def hey():
    print("code that called from fun")

#calling a function
hey()

#function with argument 

def greet(name):
    print(f"hey, {name}")

list = ["pinak" , "kirtan" , "vaibhav"]

for i in list:
    greet(i)

#function with return

def sqrt(number):
    return number*number
    
print(sqrt(3))