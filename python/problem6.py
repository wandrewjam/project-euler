"""
Project Euler Problem 6: Sum square difference
"""

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

MAXINT = 100
sumsq = 0
sqsum = (MAXINT*(MAXINT+1)//2)**2

# Calculate the sum of squares
for i in range(1,MAXINT+1):
    sumsq += i**2

print(sqsum-sumsq)
