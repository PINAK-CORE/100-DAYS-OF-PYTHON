# DAY 4 : ROCK PAPER SCISSORS

import random 

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

game_mode = input("Are you Ready To Play Rock Paper Scissors ? [1] lets roll [2] nahh : ")


while(game_mode == '1'):
    
    p1_choice = random.randint(1,3)
    print("Enter 0 to exit this Game")
    p2_choice = int(input
                    (
                        '''
                        Enter your choice 
                        [1] Rock
                        [2] Paper
                        [3] Scissors
\n
> Your Choice : '''
                    ))
    
    if(p2_choice == 0):
        break

    if(p1_choice == p2_choice ):

        if(p1_choice == 1):
            print(
                f'''
                {rock} Computer

                v/s

                {rock} YOU
                '''
            )
        if(p1_choice == 2):
            print(
                f'''
                {paper} Computer

                v/s
                
                {paper} YOU
                '''
            )
        if(p1_choice == 3):
            print(
                f'''
                {scissors} Computer

                v/s
                
                {scissors} YOU
                '''
            )

        print("Result : tie")

    elif(p1_choice == 1 and p2_choice == 2):

        print(
                f'''
                {rock} Computer

                v/s
                
                {paper} YOU
                '''
            )

        print("Result : You Win !!!")

    elif(p1_choice == 1 and p2_choice == 3):

        print(
                f'''
                {rock} Computer

                v/s
                
                {scissors} YOU
                '''
            )

        print("Result : Compter Wins !!")

    elif(p1_choice == 2 and p2_choice == 1):

        print(
                f'''
                {paper} Computer

                v/s
                
                {rock} YOU
                '''
            )

        print("Result : Computer Win !!!")

    elif(p1_choice == 2 and p2_choice == 3):

        print(
                f'''
                {paper} Computer

                v/s
                
                {scissors} YOU
                '''
            )
        
        print("Result : You Wins !!!")
    
    elif(p1_choice == 3 and p2_choice == 1):

        print(
                f'''
                {scissors} Computer

                v/s
                
                {rock} YOU
                '''
            )
        
        print("Result : You Wins !!")

    elif(p1_choice == 3 and p2_choice == 2):

        print(
                f'''
                {scissors} Computer

                v/s
                
                {paper} YOU
                '''
            )

        print("Result : Computer Wins !!")

print("\n THANK YOU FOR PLAYTING THIS GAME ")
    
