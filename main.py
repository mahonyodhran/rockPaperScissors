import random

userWins = 0
aiWins = 0

selections = ['rock', 'paper', 'scissors']

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
        
    else:
        print("You lose")
        aiWins +=1

print("\nYou won", userWins,"times")
print("The AI won", aiWins,"times")
print("Goodbye!")
    