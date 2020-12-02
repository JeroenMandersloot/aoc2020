with open('input.txt', 'r') as f:
    nums = [int(line.strip()) for line in f.readlines()]

solutions = set()

for num in nums:
    if num in solutions:
        print(num * (2020 - num))
    solutions.add(2020 - num)
