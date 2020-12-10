with open('input.txt', 'r') as f:
    jolts = [int(line.strip()) for line in f.readlines()]

sjolts = [0, *sorted(jolts), max(jolts) + 3]
diffs = [b - a for a, b in zip(sjolts[:-1], sjolts[1:])]

a = sum(d == 1 for d in diffs)
b = sum(d == 3 for d in diffs)

print(a*b)