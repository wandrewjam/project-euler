"""
Project Euler Problem 12: Highly divisible triangular number
"""

# What is the value of the first triangle number to have over five hundred divisors?


def prime_sieve(limit):
    sieve_bound = (limit - 1) // 2
    sieve = [False]*sieve_bound
    cross_limit = int(limit**(1/2) - 1) // 2
    for i in range(cross_limit):
        if not sieve[i]:
            for j in range(3+i*(6+2*i), sieve_bound, 2*i + 3):
                sieve[j] = True
    return sieve


def number_of_factors(number, prime_list):
    if number < 2:
        return 1
    if number == 2:
        return 2
    if number == 3:
        return 2
    factors = 1
    p_index = 0
    p = prime_list[p_index]
    while p**2 <= number and number % p == 0:
        factor_count = 0
        number //= p
        factor_count += 1
        factors *= factor_count
        p_index += 1
        p = prime_list[p_index]
    return factors


START = 10
number_divisors = 0
i = 0

# limit = 3
# sieve = prime_sieve(limit)
primes = [2, 3, 5]
print(prime_factor(5, primes))
# for i in range(len(sieve)):
#     if not sieve[i]:
#         prime_list.append(2*i+3)
#
# while number_divisors < 500:
#     triangular_number = (START+i)*(START+i+1)/2
