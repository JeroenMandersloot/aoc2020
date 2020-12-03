import numpy as np

with open('input.txt', 'r') as f:
    m = np.array([[0 if c == '.' else 1 for c in line.strip()] for line in f.readlines()], dtype=bool)
   

x = y = 0
height, width = m.shape
step_x = 3
step_y = 1

num_trees = 0
while y < height:
    num_trees += m[y, x]
    y += step_y
    x = (x + step_x) % width

print(num_trees)