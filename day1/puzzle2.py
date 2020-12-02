from typing import List
from functools import reduce

with open('input.txt', 'r') as f:
    nums = [int(line.strip()) for line in f.readlines()]


def aap(nums: List[int], total: int, n: int) -> int:
    if n > 2:
        for num in nums:
            if res := aap(nums, total - num, n - 1):
                return [num, *res]
    
    elif n == 2:
        solutions = set()
        for num in nums:
            if num in solutions:
                return [num, total - num]
            solutions.add(total - num)
            
    return None
    
res = aap(nums, 2020, 3)

print(res)
print(reduce(lambda a, b: a * b, res, 1))