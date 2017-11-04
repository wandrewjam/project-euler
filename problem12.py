"""
Project Euler Problem 12: Highly divisible triangular number
"""

# What is the value of the first triangle number to have over five hundred divisors?

START = 10
prime_list = [2, 3, 5, 7]
number_divisors = 0
i = 0

while number_divisors < 500:
    triangular_number = (START+i)*(START+i+1)/2
    while triangular_number > prime_list[-1]**2:
        isPrime = False
        while not isPrime:


