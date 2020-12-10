from functools import lru_cache

with open('input.txt', 'r') as f:
    jolts = [int(line.strip()) for line in f.readlines()]


@lru_cache(maxsize=None)
def get_num_arrangements(sorted_jolts, start):
    if not sorted_jolts:
        return 1
    if sorted_jolts[0] > start + 3:
        return 0
        
    res = 0
    for i, jolt in enumerate(sorted_jolts):
        if jolt <= start + 3:
            res += get_num_arrangements(sorted_jolts[i+1:], jolt)
        else:
            break
    return res
    

sjolts = tuple([*sorted(jolts), max(jolts) + 3])
print(get_num_arrangements(sjolts, 0))