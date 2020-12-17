import numpy as np
from itertools import product
from tqdm import tqdm

num_cycles = 6

with open('dummy_input.txt', 'r') as f:
	initial = np.array([[c == '#' for c in line.strip()] for line in f.readlines()])
    
dims = tuple(reversed((*initial.shape, 1, 1)))
grid = np.zeros(dims, dtype=bool)
grid[0, 0] = initial



def get_neighbours(w, z, y, x, grid):
    for nw, nz, ny, nx in product(*(set(map(lambda d: max(min(d, s-1), 0), [c-1, c, c+1])) for s, c in zip(grid.shape, [w, z, y, x]))):
        if (nw, nz, ny, nx) != (w, z, y, x):
            yield grid[nw, nz, ny, nx]
    

for i in tqdm(range(num_cycles)):
    g = np.zeros(tuple(map(lambda d: d+2, grid.shape)), dtype=bool)
    print(g.shape)
    g[1:-1, 1:-1, 1:-1, 1:-1] = grid
    grid = g
    new_grid = np.copy(grid)
    for w, z, y, x in product(*map(range, dims)):
        current = grid[w, z, y, x]
        num_active_neighbours = sum(get_neighbours(w, z, y, x, grid))
        is_active = current
        if current and num_active_neighbours not in (2, 3):
            is_active = False
        elif not current and num_active_neighbours == 3:
            is_active = True
        new_grid[w, z, y, x] = is_active
    grid = new_grid


print(np.sum(grid))