"""
Project Euler Problem 7: 10,001st prime
"""

# What is the 10,001st prime number?

# NOTE: this solution implements the pseudocode explained in the posted solutions on projecteuler.net
#                                                           url: (https://projecteuler.net/overview=007)


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n%2 == 0:
        return False
    elif n < 9:
        return True
    elif n%3 == 0:
        return False
    else:
        r = int(n**(1/2))
        f = 5
        while f <= r:
            if n%f == 0:
                return False
            elif n%(f+2) == 0:
                return False
            f += 6
        return True


limit = 10001
count = 1
candidate = 1
while count < limit:
    candidate += 2
    if is_prime(candidate):
        count = count + 1

print(candidate)
