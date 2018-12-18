"""
Project Euler Problem 12: Highly divisible triangular number
"""

# What is the value of the first triangle number to have over five hundred divisors?

# A simple solution is to not worry about generating primes, and just test odd numbers for divisors
# Since we have to test a lot of numbers, it probably is worth generating a list of primes

START = 1
number_divisors = 0
i = 0

while number_divisors < 500:
    i += 1
    powers = []
    tri_number = (START+i)*(START+i+1)/2
    power = 0
    while tri_number % 2 == 0:
        power += 1
        tri_number /= 2
    if power > 0:
        powers.append(power)
    factor = 3
    while tri_number > 1:
        power = 0
        while tri_number % factor == 0:
            power += 1
            tri_number /= factor
        factor += 2
        if power > 0:
            powers.append(power)
    number_divisors = 1
    for p in powers:
        number_divisors *= p + 1

print((START+i)*(START+i+1)//2)
