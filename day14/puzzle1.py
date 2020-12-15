import re

mem = dict()

with open('input.txt', 'r') as f:
    mask = None
    for line in f.readlines():
        line = line.strip()
        if line.startswith('mem'):
            if not mask:
                raise ValueError("Mask not initialized")
            address, value = map(int, re.match(r'^mem\[(\d+)\] = (\d+)$', line).groups())
            binary = str(bin(value))[2:].rjust(36, '0')
            result = "".join(b if m == 'X' else m for m, b in zip(mask, binary))
            mem[address] = int(result, 2)
        if line.startswith('mask'):
            mask = re.match(r'^mask = ([01X]+)$', line).groups()[0]
            
print(sum(mem.values()))