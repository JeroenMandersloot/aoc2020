from typing import List, Tuple

instructions = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        instruction, value = line.strip().split(' ')
        value = int(value[1:]) if value.startswith('+') else int(value)
        instructions.append((instruction, value))
    


def run_instructions(instructions: List[Tuple[str, int]]):
    acc = 0
    i = 0
    mem = set()
    while True:
        if i == len(instructions):
            return acc
        instruction, value = instructions[i]
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


for i, (instruction, value) in enumerate(instructions):
    if instruction == 'jmp':
        candidate = instructions[:]
        candidate[i] = ('nop', value)
        try:
            print(run_instructions(candidate))
            break
        except ValueError:
            pass
    elif instruction == 'nop':
        candidate = instructions[:]
        candidate[i] = ('jmp', value)
        try:
            print(run_instructions(candidate))
            break
        except ValueError:
            pass
    