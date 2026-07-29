print("Welcome to Treasure Island. ")
print("Your Mission is to find the treasure!")

choice1 = input("You are at a cross road. Where do you want to go? \n \t\t Type 'left' or 'right' ").lower()
if (choice1 == 'left'):
    choice2 = input('You\'ve come to a lake....'
                    'Type "Wait" to wait for the boat....'
                    'Type "Swim" to swim across  ').lower()
    if(choice2 == "wait"):
        #game will continue
        choice3 = input('You arrive at the island unharmed. ' 
                        'There is a house with 3 doors. One Red, '
                        'one yellow and one blue '
                        'Which colour do you choose   ').lower()
        if(choice3 == 'red'):
            print("It is room full of fire. Game Over!")
        elif(choice3 == 'yellow'):
            print("You found the treasure !!!")
        elif(choice3 == 'blue'):
            print("You enetered a room full of beasts. Game Over!")
    else:
        print("You got attacked by an angry croc. Game Over !!")
else:
    print("You fell in a hole. Game Over!")