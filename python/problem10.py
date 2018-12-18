"""
Project Euler Problem 10: Summation of primes
"""

# Find the sum of all the primes below two million

MAX = 2e6
primeList = [2, 3]
nextPrime = primeList[-1]

while nextPrime + 2 < MAX :
    # Find the next prime
    isPrime = False
    while not isPrime:
        nextPrime += 2
        isPrime = True
        k = 0
        while primeList[k]**2 <= nextPrime and isPrime:
            if nextPrime%primeList[k] == 0:
                isPrime = False
            k += 1
    if nextPrime < MAX:
        primeList.append(nextPrime)
print(sum(primeList))
