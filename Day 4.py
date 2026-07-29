import random


# hc=0
# tc=0
# for i in range(0,100):
#     toss = random.randint(0,1)
#     if( toss == 0):
#         hc+=1
#     if(toss == 1):
#         tc+=1
# print(hc,tc)


''' ////////////////////////////////////////// '''

# #Banker Roullette
# friends = ['Alice' , 'Bob', 'Charlie', 'David', 'Emanuel']

# #option 1
# print(friends[random.randint(0,len(friends)-1)])

# #option 2
# print(random.choice(friends))

'''/////////////////////////////////////////////////// '''

#ROCK PAPER SCISSOR GAME
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("What do you choose?")
print("Type 0 for Rock")
print("Type 1 for Paper")
print("Type 2 for Scissors")
choice = int(input("What did you choose?        "))
comp_choice = random.randint(0,2)

if(choice not in [0,1,2]):
    print("You have not entered a valid input, pls try again.")

if(choice == comp_choice):
    print("This is a draw, try again")

# scenarios
if (choice == 0 ):
    print("You chose Rock: \n")
    print(rock)
    if (comp_choice == 1):
        print("Computer chose Paper: \n")
        print(paper)
        print("You lost")
    elif(comp_choice == 2):
        print("Computer chose Scissors: \n")
        print(scissor)
        print("You win!") 


elif(choice == 1):
    print("You chose Paper: \n")
    print(paper)
    if(comp_choice == 0):
        print("Computer chose Rock: \n")
        print(rock)
        print("You win!")
    elif(comp_choice == 2):
        print("Computer chose Scissors: \n")
        print(scissor)
        print("You lost")


elif(choice == 2):
    print("You chose Scissors: \n")
    print(scissor)
    if(comp_choice == 0):
        print("Computer chose Rock: \n")
        print(rock)
        print("You lost")
    elif(comp_choice == 1):
        print("Computer chose Paper: \n")
        print(paper)
        print("You win!")