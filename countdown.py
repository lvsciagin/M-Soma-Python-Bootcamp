#Get a number and count down to 0
#define function
def numberChecker(string):
    #for error handling
    try:
        isNumber = int(string)
        return True 
        #is number checker a py function
    except ValueError:
        print ("Value entered is Not an integer!")
        return False

user_input = input("Enter your input: ")
isNumber = False

while not isNumber:
    if(numberChecker(user_input)):
        isNumber = True
        i_input = int(user_input)
    else:
        user_input = input("Please enter an integer. ")
        
while(i_input < 0):
    user_input = input("Enter a positive number. ")
    #Need to check if input is a number again
    isNumber = False
    while not isNumber:
        if(numberChecker(u_input)):
            isNumber = True
            i_input = int(u_input)
        else:
            u_input = raw_input("Please enter an integer. ")
    i_input = int(user_input)):
    try:
        isNumber = int(string)
        return True
    except ValueError:
        print ("Not an integer")
while(i_input >= 0):
    print (i_input)
    i_input -= 1