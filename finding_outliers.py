"""
upper_limit = 100
lower_limit = 10

user input of limit

result_outlier

lets check if the input value is in between the upper or lower limit. 
If not, we will print the result_outlier
"""

# Finding outliers
# date: 2021-07-07
# author: M. Meckatzer
# version: 1.0

upper_limit = 100
lower_limit = 10

user_input = int(input("Enter a number: "))


if user_input < lower_limit:
    result_outlier = True

if user_input > upper_limit:
    result_outlier = True

if result_outlier:
    print("The number is an outlier")
else:
    print("The number is not an outlier")