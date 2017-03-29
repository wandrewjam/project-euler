"""
Project Euler Problem 4: Largest palindrome product
"""

# Find the largest palindrome made from the product of two 3-digit numbers

palindrome = 1

for i in range(100,1000):
    for j in range(i,1000):     # Iterate over all pairs of 3-digit numbers
        prod = i*j
        if (str(prod) == str(prod)[::-1]) and i*j > palindrome: # If the product is a palindrome, and larger than the
            palindrome = i*j                                # currently stored palindrome, then update the palindrome


print(palindrome)
