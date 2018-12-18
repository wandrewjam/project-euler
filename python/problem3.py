"""
Project Euler Problem 3: Largest Prime Factor
"""

# What is the largest prime factor of the number 600851475143?

number = 600851475143

prime_list = [2]        # Declare the list of prime numbers
i = 3       # First prime number
j = 0       # Initialize index counter

while i**2 <= number:       # The largest possible prime factor is <= sqrt(number)
    isPrime = True
    while prime_list[j]**2 <= i:        # We check that i is divisible by lower prime numbers
        if i % prime_list[j] == 0:
            isPrime = False             # If i is divisible by something, it is not prime

        j += 1
    if isPrime:
        prime_list.append(i)        # If i is prime, add it to the list
    if isPrime and number % i == 0:
        number = number // i        # If i is prime, and divides 'number', then divide the two and make that 'number'
    i += 2

print(number)
