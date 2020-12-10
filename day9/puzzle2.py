with open('input.txt', 'r') as f:
    memory = [int(line.strip()) for line in f.readlines()]
    

def find_contiguous_sum(num):
    for i, start in enumerate(memory):
        s = start
        j = i + 1
        while s < num:
            s += memory[j]
            j += 1
        if s == num:
            return memory[i:j]


res = find_contiguous_sum(177777905)
print(min(res) + max(res))