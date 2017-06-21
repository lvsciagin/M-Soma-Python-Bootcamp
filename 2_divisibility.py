s_number = raw_input("Enter a number that's divisible by two. ")
isNumber = numberChecker(s_number)
while not isNumber:
    s_number = raw_input("That's not even a number. Try again. ")
    isNumber = numberChecker(s_number)
i_number = int(s_number)
while i_number % 2 != 0:
    s_number = raw_input("That's not divisible by two. Try again. ")
    isNumber = numberChecker(s_number)
    while not isNumber:
        s_number = raw_input("That's not even a number. Try again. ")
        isNumber = numberChecker(s_number)
    i_number = int(s_number)
print "Yes, " + s_number + " is divisble by 2."
