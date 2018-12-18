"""
Project Euler Problem 8: Largest product in a series
"""

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

number = open('number')
numStr = number.read()
numStr = "".join(numStr.split())        # Eliminates all whitespace in the string

maxProd = 0

for i in range(0,len(numStr)-13):
    prod = 1
    for j in range(0,13):
        prod *= int(numStr[j+i])
    if prod > maxProd:
        maxProd = prod

print(maxProd)
