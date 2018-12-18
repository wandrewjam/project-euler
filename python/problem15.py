"""
Project Euler Problem 15: Lattice Paths
"""

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly
#   6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?

GRID_SIZE = (2, 2)

horz, vert = GRID_SIZE
path = [0]*horz + [1]*vert
path_count = 1

while path[0] == 0:


print(path)
