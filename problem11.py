"""
Project Euler Problem 11: Largest product in a grid
"""

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

grid = open('grid.txt')
gStr = grid.read()
gStr = gStr.split()
g = [0]*len(gStr)

for i in range(0,len(gStr)):
    g[i] = int(gStr[i])

maxproduct = 0

for i in range(0,20):
    for j in range(0,20):
        if (i<17):
            prod = g[20*i+j]*g[20*(i+1)+j]*g[20*(i+2)+j]*g[20*(i+3)+j]
            if (prod > maxproduct):
                maxproduct = prod
        if (i<17) and (j<17):
            prod = g[20*i+j]*g[20*(i+1)+j+1]*g[20*(i+2)+j+2]*g[20*(i+3)+j+3]
            if (prod > maxproduct):
                maxproduct = prod
        if (j<17):
            prod = g[20*i+j]*g[20*i+j+1]*g[20*i+j+2]*g[20*i+j+3]
            if (prod > maxproduct):
                maxproduct = prod
        if (i>2) and (j<17):
            prod = g[20*i+j]*g[20*(i-1)+j+1]*g[20*(i-2)+j+2]*g[20*(i-3)+j+3]
            if (prod > maxproduct):
                maxproduct = prod
print(maxproduct)
