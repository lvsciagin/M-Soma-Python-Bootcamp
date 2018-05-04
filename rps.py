import random

print("Rock Paper Scissors")

winning = False

while winning == False:
    print("")
    print("1 = Rock.")
    print("2 = Paper.")
    print("3 = Scissors.")

    users = int(input("Select to play?"))
    comp = random.randrange(1,3)

    if (users == 1) and (comp == 1):
        winning = False
        print("Draw;both played Rock!")
        
    if (users == 2) and (comp == 1):
        winning == True
        print("You win! Computer played Rock!")

    if (users == 3) and (comp == 1):
        winning == True
        print("You lose! Computer played Rock!")
        
    if (users == 1) and (comp == 2):
        winning = True
        print("You lose! Computer played Paper!")
        
    if (users == 2) and (comp == 2):
        winning == False
        print("Draw; computer played Paper!")

    if (users == 3) and (comp == 2):
        winning == True
        print("You win! Computer played Paper!")
        
    if (users == 1) and (comp == 3):
        winning = True
        print("You win! Computer played Scissors!")
        
    if (users == 2) and (comp == 3):
        winning == True
        print("You lose! Computer played Scissors!")

    if (users == 3) and (comp == 3):
        winning == False
        print("Draw; Computer played Scissors!")