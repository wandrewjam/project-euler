"""
Project Euler Problem 9: Special Pythagorean triplet
"""

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

SUM = 1000
foundTriple = False
m = 1

while not foundTriple:
    m += 1
    for n in range(1,m):
        if SUM%(2*m*(m + n)) == 0:
            foundTriple = True
            break

a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2       # Use Euclid's formula to generate Pythagorean triples
k = SUM // (a + b + c)

print(a, b, c)
print(k**3*a*b*c)
