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
            binary = str(bin(address))[2:].rjust(36, '0')
            result = "".join(b if m == '0' else m for m, b in zip(mask, binary))
            addresses = [""]
            for i, c in enumerate(result):
                if c == 'X':
                    addresses = [x for a in addresses for x in [f"{a}0", f"{a}1"]]
                else:
                    addresses = [f"{a}{c}" for a in addresses]
            for address in addresses:
                mem[int(address, 2)] = value
        if line.startswith('mask'):
            mask = re.match(r'^mask = ([01X]+)$', line).groups()[0]
            
print(sum(mem.values()))