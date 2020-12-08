instructions = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        instruction, value = line.strip().split(' ')
        value = int(value[1:]) if value.startswith('+') else int(value)
        instructions.append((instruction, value))


acc = 0
i = 0
mem = set()
while True:
    instruction, value = instructions[i]
    print(f"{i}. {instruction} {value}")
    if i in mem:
        raise ValueError(f"Instruction {i} is about to be executed twice. Acc: {acc}")
    mem.add(i)
    if instruction == 'acc':
        acc += value
        i += 1
    elif instruction == 'jmp':
        i += value
    elif instruction == 'nop':
        i += 1