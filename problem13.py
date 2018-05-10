"""
Project Euler Problem 13: Large sum
"""

# Work out the first ten digits of the sum of the given list of one-hundred 50-digit numbers

# This is the trivial solution

numberFile = open('number_list.txt')
numberStr = numberFile.read()
numberStr = numberStr.split()

big_sum = 0
for num in numberStr:
    big_sum += int(num)

sumStr = str(big_sum)
print(sumStr[0:10])
