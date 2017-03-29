"""
Project Euler Problem 5: Smallest multiple
"""

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MAXFACTOR = 20
divisible = False
number = 0

while not divisible:
    number += MAXFACTOR
    divisible = True
    for i in range(2,MAXFACTOR+1):
        if number%i != 0:
            divisible = False
            break

print(number)
