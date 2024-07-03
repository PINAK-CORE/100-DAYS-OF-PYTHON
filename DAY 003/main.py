# DAY 3 Treasure Island


game_mode = int(input("\n ARE YOU READY ?? [1] hell yea [2] nahh im normal : "))

if(game_mode == 1):
    print(''' Welcome to Treasure Island. 
        Your mission is to find the treasure.
        ''')
    
    while(game_mode == True):
        choice1 = input
        (
            ''' 
            [1] GO Right
            [2] GO left
            '''
        )
        if(choice1 == '1' or choice1 == 'right'):
            print
            (
            '''
            Fall into a hole.
            Game Over.
            '''
            )
            break
        else:
            choice2 = input
            (
                '''
                That was eazy now there is a Lake What you wanna do swim like champ or wait like waiter
                [1] swim
                [2] wait
                '''
            )
            if(choice2 == '1' or choice2 == 'swim'):
                print
                (
                    ''' 
                    Attacked by trout.
                    Game Over.
                    '''
                )
                break
            else:
                print("NOO WAYYY YOU PASSED THIS TRICK ...!!!")

                choice3 = input
                (
                    '''
                    ok ! last Stage !!!
                    there are three door ... red , green , yellow choose one of them you can escape
                    [1] red
                    [2] blue
                    [3] yellow
                    '''
                )
                if(choice3 == '1' or choice3 == "red"):
                    print
                    (
                        '''
                        Burned by fire. 🔥
                        Game Over.
                        '''
                    )
                    break
                elif(choice3 == '2' or choice3 == "blue"):
                    print
                    (
                        '''
                        Eaten by beasts.
                        Game Over.
                        '''
                    )
                    break
else:
    print("ok losser 😛")
    
