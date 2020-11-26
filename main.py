
# Rock Paper Scissors Game

#Random values
import random
#Miscellaneous operating system interfaces
import os
#Regex
import re

os.system('cls' if os.name=='nt' else 'clear')
exit = False
while(exit == False):
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper or [S]cissors (To exit press [E]): ")
    if not re.match("[SsRrPpeE]",userChoice):
        print("Please Choose  Letter:")
        print("[R]ock, [P]aper, [S]cissors or [E]xit")
    # Echo the user's choice
    if userChoice.upper() == "E":
        print("Goodbey!")
        exit = True
        break
    else:
        print("You choose: ", str.upper(userChoice))
        choices = ['R','P','S']
        opponentChoices = random.choice(choices)
        print("I choose: ", opponentChoices)
        if opponentChoices == str.upper(userChoice):
            print("Tie!")
        elif opponentChoices == 'R' and userChoice.upper() == 'S':
            print("Rock beats Scissor, I win!")
            continue
        elif opponentChoices == 'S' and userChoice.upper() == 'P':
            print("Scissors beats Paper, I win!")
            continue
        elif opponentChoices == 'P' and userChoice.upper() == 'R':
            print("Paper beats Rock, I win!")
            continue
        else:
            print("You win!")
