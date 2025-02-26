# # city = "Ich bin in FN!!!!!"
# # company = "Microsoft"
# # job_title = "Engineer"
# name = "Daniel"
# last_name = "Schäftner" 
# full_name = name + last_name

# print("My name is: \"in Anführungszeichen\" ")

# active_users = 0.5
# stundents_in_class = 45
# print(stundents_in_class / active_users)

# powered_on = False

# print(not powered_on)

# entered_pin = 5444
# expected_pin = 5555
# result = entered_pin != expected_pin


# number_1 = 14
# number_2 = 13

# result = number_1 >= number_2

# print(result)
item_1 = "meckatzer"
item_2 = "augustiner"

# is_dublicated = item_1 == item_2

# text = "string"
anzahl = 5
kosten = 1.6778
# boolsche = True

# formated print
# print(f"{anzahl} meckatzer für {kosten}€ bitte")

# print( str(anzahl) + " messgage")

# val = input("Enter a value: ")
# print(val)
# print("git")

# condition = False

# if condition:
#     print("condition is true")

# age = int(input("Enter your age: "))

# if (age >= 18):
#     print("You are an adult")

# hour = int(input("Enter the hour: "))

# if hour < 12:
#     print("Good morning")
# elif hour < 18:
#     print("Good afternoon")
# elif hour < 22:
#     print("Good evening")
# else:
#     print("Good night")

age = int(input("Enter your age: "))
has_permission = True
has_license = True	
alcohol_level = 0.5
has_insurance = True

if (18 <= age) and ((True == has_permission) or (has_license == True)) and (alcohol_level <= 0.3) and has_insurance:
    print("You are allowed to drive")
