'''Wir wollen Meilen in Kilometer umrechnen und ausgeben.
Bitte schreibe das Programm'''

# Author: Daniel Schäftner.
# Date: 16.01.2025

### CONSTANTS
FACTOR = 1.60934 # this is the factor miles to km

### PROGRAMM

# Inputs
miles = float(input("Enter miles: "))

# Process
km = miles * FACTOR  

# Output
print("This is your result in km: " + str(km))