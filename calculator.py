##################################################
##                                              ##
## Taschenrechner / Calculator                  ##
##                                              ##
##################################################

# author: 31.01.2022 Daniel Schäftner
# brief: Calculator with 4 basic operations

##################################################
# Usermenue input                                #
##################################################

try:
    number_1 = float(input("1. Zahl: "))
    number_2 = float(input("2. Zahl: "))
except ValueError:
    error = True

operation = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")

#################################################
# Calculation                                   #
#################################################

result = 0
error = False

# Add
if operation == '+':
    result = number_1 + number_2

# Sub
elif operation == '-':
    result = number_1 - number_2

# Mult
elif operation == '*':
    result = number_1 * number_2

# Div
elif operation == '/':
    # check for division by zero
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        error = True

# wrong operation
else:
    error = True

#################################################
# Result output                                 #
#################################################

if not error:
    print(f"Das Ergebnis ist: {result}")
else:
    print("Rechenoperation nicht unterstützt!")
