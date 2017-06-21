# Rock Paper Scissors

from random import randint
 
#create a list of play options and assign to variable 'Play'
Play = ["Rock", "Paper", "Scissors"]
 
#Let computer randomize selection within the array and assign it to variable computer
computer = Play[randint(0,2)]
 
#set player to False( player hasnt played yet computer waiting for player's input)
player = False

#start the while loop
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?\n\t")
    if player == computer:
        print("Tie!\n\tLogic? Computer randomized a play similar to yours")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!\n\tLogic?", computer, "covers", player, "\n\t\tPlay again")
        else:
            print("You win!\n\tLogic?", player, "smashes", computer, "\n\t\tPlay again")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!\n\tLogic?", computer, "cut", player, "\n\t\tPlay again")
        else:
            print("You win!\n\tLogic?", player, "covers", computer, "\n\t\tPlay again")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!\n\tLogic?", computer, "smashes", player, "\n\t\tPlay again")
        else:
            print("You win!\n\tLogic?", player, "cut", computer, "\n\t\tLogicPlay again")
    else:
        print("Invalid selection. Check your spelling. The input is case sensitive!")

    #Reinitialize player back to 'False' so that the loop continues

    player = False
    computer = Play[randint(0,2)] 

