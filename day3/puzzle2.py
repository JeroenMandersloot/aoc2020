import numpy as np
from functools import reduce, partial

with open('input.txt', 'r') as f:
    m = np.array([[0 if c == '.' else 1 for c in line.strip()] for line in f.readlines()], dtype=bool)


def get_num_trees(step_x: int, step_y: int) -> int:
    x = y = 0
    height, width = m.shape

    num_trees = 0
    while y < height:
        num_trees += m[y, x]
        y += step_y
        x = (x + step_x) % width

    return num_trees
  
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
all_num_trees = [get_num_trees(*slope) for slope in slopes]

print(all_num_trees)
# Casting to np.uint64 is a dirty hack to bypass python's max int value
print(int(reduce(lambda a, b: a*b, map(partial(np.array, dtype=np.uint64), all_num_trees), 1)))

