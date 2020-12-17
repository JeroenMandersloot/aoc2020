import numpy as np
from itertools import product

num_cycles = 6

with open('input.txt', 'r') as f:
	initial = np.array([[c == '#' for c in line.strip()] for line in f.readlines()])
    
grid = np.zeros(tuple(reversed((*initial.shape, 1))), dtype=bool)
grid[0] = initial



def get_neighbours(z, y, x, grid):
    for nz, ny, nx in product(*(set(map(lambda d: max(min(d, s-1), 0), [c-1, c, c+1])) for s, c in zip(grid.shape, [z, y, x]))):
        if (nz, ny, nx) != (z, y, x):
            yield grid[nz, ny, nx]
    
    
for i in range(num_cycles):
    g = np.zeros(tuple(map(lambda d: d+2, grid.shape)), dtype=bool)
    g[1:-1, 1:-1, 1:-1] = np.copy(grid)
    grid = np.copy(g)
    new_grid = np.copy(grid)
    for z, y, x in product(*map(range, grid.shape)):
        current = grid[z, y, x]
        num_active_neighbours = sum(get_neighbours(z, y, x, grid))
        is_active = current
        if current and num_active_neighbours not in (2, 3):
            is_active = False
        elif not current and num_active_neighbours == 3:
            is_active = True
        new_grid[z, y, x] = is_active
    grid = new_grid


print(np.sum(grid))