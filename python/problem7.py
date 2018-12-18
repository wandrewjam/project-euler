"""
Project Euler Problem 7: 10,001st prime
"""

# What is the 10,001st prime number?

k = 10001

if k == 1:
    print(2) # The first prime is 2
else:
    primeList = [2, 3]
    nextPrime = 3
    while len(primeList) < k:
        isPrime = False
        while not isPrime:
            nextPrime += 2
            isPrime = True
            i = 0
            while primeList[i]**2 <= nextPrime and isPrime:
                if nextPrime%primeList[i] == 0:
                    isPrime = False
                i += 1
        primeList.append(nextPrime)
    print(primeList[-1])
