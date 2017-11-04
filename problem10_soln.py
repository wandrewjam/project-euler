"""
Project Euler Problem 10: Summation of primes
"""

# Find the sum of all the primes below two million

# NOTE: this solution implements the pseudocode explained in the posted solutions on projecteuler.net
#                                                           url: (https://projecteuler.net/overview=010)

from timeit import default_timer as timer


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


start = timer()
limit = 2*10**6
sum = 5
n = 5
while n <= limit:
    if is_prime(n):
        sum += n
    n += 2
    if n <= limit and is_prime(n):
        sum += n
    n += 4
end = timer()

print('Sum is: ', sum)
print('Elapsed time: ', end - start)


start = timer()
sieve_bound = (limit - 1) // 2
sieve = [False]*sieve_bound
cross_limit = int(limit**(1/2) - 1) // 2
for i in range(cross_limit):
    if not sieve[i]:
        for j in range(3+i*(6+2*i), sieve_bound, 2*i + 3):
            sieve[j] = True
sum = 2
for i in range(sieve_bound):
    if not sieve[i]:
        sum += 2*i + 3
end = timer()
print('\nSum is ', sum)
print('Elapsed time: ', end - start)
