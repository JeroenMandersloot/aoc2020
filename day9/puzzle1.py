def is_valid(num, preamble):
    preamble = set(preamble)
    for n in preamble:
        if num - n in preamble and num != n:
            return True
    return False


p = 25
with open('input.txt', 'r') as f:
    memory = []
    for i, line in enumerate(f.readlines()):
        num = int(line.strip())
        print(f"{i}: {num}")
        if i >= p and not is_valid(num, memory[-p:]):
            print(num)
            break
        memory.append(num)