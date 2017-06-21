base = input("Raise... ")
exp = input("to the power of... ")
isNumber = numberChecker(base) and numberChecker(exp)
while not isNumber:
    base = input("Please enter a base that's a number. ")
    exp = input("Please enter an exponent that's a number. ")
    isNumber = numberChecker(base) and numberChecker(exp)
i_base = int(base)
i_exp = int(exp)
answer = 1
for i in range(i_exp):
    answer *= i_base
if i_base == 0:
    answer = 0
if i_exp == 0:
    answer = 1
print (base + " raised to the power of " + exp + " is " + str(answer))
