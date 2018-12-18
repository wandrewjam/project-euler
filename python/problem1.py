"""
Project Euler Problem 1: Multiples of 3 and 5
"""

# Find the sum of all the multiples of 3 or 5 below 1000

MAX = 1000
sum = 0

# Simple brute force
for i in range(1,MAX):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
