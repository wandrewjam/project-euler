"""
Project Euler Problem 14: Longest Collatz sequence
"""

# Which starting number under one million produces the longest Collatz chain?

# The simple solution


from timeit import default_timer as timer


start = timer()
def collatz_counter(start):
    # Function to count the number of terms in a Collatz sequence starting with 'start'
    counter = 1  # Initialize the counter
    while start != 1:
        if start % 2 == 0:  # If the number is even
            start /= 2
            counter += 1
        else:  # If the number is odd
            start = 3*start + 1
            counter += 1
    return counter


top = 10**5 - 1
maximum = 1
for i in range(1, top):
    counter = collatz_counter(i)
    if counter > maximum:
        max_start = i
        maximum = counter
end = timer()

print(max_start)
print(end - start)

# A faster solution

start = timer()


def collatz(start):
    collatz_list = [start]
    while collatz_list[-1] != 1:
        if collatz_list[-1] % 2 == 0:
            collatz_list.append(collatz_list[-1]//2)
        else:
            collatz_list.append(3*collatz_list[-1] + 1)
    return collatz_list


top = 10**5 - 1
array = [True] * (top - 1)
max_length = 1
max_start = 1
for i in range(top - 1):
    if array[i]:
        collatz_list = collatz(i + 1)
        for el in collatz_list:
            if el < top:
                array[el - 1] = False
        if len(collatz_list) > max_length:
            max_length = len(collatz_list)
            max_start = i + 1

end = timer()

print(max_start)
print(end - start)
