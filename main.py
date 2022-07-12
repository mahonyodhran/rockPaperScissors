import random
from User import User

userWins = 0
aiWins = 0
draws = 0
selections = ['rock', 'paper', 'scissors']

user = User(input('Hello! Before we start, what is your name: '))
if(user.name.strip() == ""):
    user.name = "Joe Bloggs"

while True:
    userSelection = input("Enter Rock/Paper/Scissors to play or Q to quit: ").lower()
    if userSelection == "q":
        break
    
    if userSelection not in selections:
        continue
    
    aiSelection = selections[random.randint(0,2)]
    print('AI picked', aiSelection)
    
    if userSelection == "rock" and aiSelection == "scissors":
        print("You win!")
        userWins += 1
    
    elif userSelection == "paper" and aiSelection == "rock":
        print("You win!")
        userWins += 1
        
    elif userSelection == "scissors" and aiSelection == "paper":
        print("You win!")
        userWins += 1
        
    elif userSelection == aiSelection:
        print("Its a draw!")
        draws += 1
        
    else:
        print("You lose")
        aiWins +=1

print("\n" + user.name + " won", userWins,"times")
print("The AI won", aiWins,"times")
print("There were", draws,"draws")
print("\nGoodbye!")
    