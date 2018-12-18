"""
Project Euler Problem 2: Even Fibonacci numbers
"""

# Find the sum of the even-valued terms of the Fibonacci sequence whose values do not exceed 4 million

sum = 0

j = 1
k = 1   # Initialize the Fibonacci sequence

# The straightforward solution
while k <= 4e6:
    if k % 2 == 0:
        sum += k
    j, k = k, j+k       # Calculate the next Fibonacci number

print(sum)
