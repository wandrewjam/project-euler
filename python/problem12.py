"""
Project Euler Problem 12: Highly divisible triangular number
"""

# What is the value of the first triangle number to have over five hundred divisors?

def sieve(limit):
    sieve_bound = (limit - 1) // 2
    sieve = [False]*sieve_bound
    cross_limit = int(limit**(1/2) - 1) // 2
    for i in range(cross_limit):
        if not sieve[i]:
            for j in range(3+i*(6+2*i), sieve_bound, 2*i + 3):
                sieve[j] = True
    return sieve


TARGET_DIVISORS = 500
number_divisors = 0
i = 32
initial_sieve = sieve(TARGET_DIVISORS)
prime_list = [2]

for j in range(len(initial_sieve)):
    if not initial_sieve[j]:
        prime_list.append(2*j + 3)

while number_divisors < TARGET_DIVISORS:
    t_number = i*(i+1)//2

    last_prime = prime_list[-1]
    while last_prime**2 < t_number:
        last_prime += 2
        k = 0
        isPrime = True
        while (prime_list[k]**2 < last_prime) and isPrime:
            if last_prime % prime_list[k] == 0:
                isPrime = False
            k += 1
        if isPrime:
            prime_list.append(last_prime)

    factorization = []
    j = 0
    while t_number > 1:
        if j >= len(prime_list):
            factorization.append(t_number)
            break

        if t_number % prime_list[j] == 0:
            t_number //= prime_list[j]
            factorization.append(prime_list[j])
        else:
            j += 1
    i += 1

    number_divisors = 1
    count = 1
    for l in range(len(factorization)):
        if l == 0:
            count += 1
        elif factorization[l] == factorization[l-1]:
            count += 1
        else:
            number_divisors *= count
            count = 2

        if l == len(factorization) - 1:
            number_divisors *= count

print(i*(i-1)//2)
