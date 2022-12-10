#!/usr/bin/python3
#
# Advent of Code 2022
# Day 10, part 1 and 2
# https://github.com/krcs/aoc-2022
#
input = "./input.txt"

def read_lines(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append(line.strip())

            if not line:
                break
    return result

lines = read_lines(input)

X = 1
cycle = 1

instruction_pointer= 0
instruction, V = [ None, None ]
end_execution_cycle = 0

signal_strength_sum = 0

sprite_position = range(X - 1, X + 2)
crt_row = 0
CRT = [[]]
pixel_idx = 0

while True:

    if instruction_pointer >= len(lines): 
        break

    if not instruction:
        instruction, *arg = lines[instruction_pointer].split(' ')

        if instruction == 'noop':
            end_execution_cycle = cycle
        elif instruction == 'addx':
            end_execution_cycle = cycle + 1
            if arg:
                V = int(arg[0])

        instruction_pointer += 1

    CRT[crt_row] += "#" if pixel_idx in sprite_position else "."

    if cycle % 40 == 0:
        crt_row += 1
        pixel_idx = 0
        CRT.append([])
    else:
        pixel_idx += 1

    if (cycle + 20) % 40 == 0:
        signal_strength_sum += cycle * X

    if cycle == end_execution_cycle:
        if instruction == 'addx':
            X += V
        end_execution_cycle = 0
        instruction, V  = [ None, None ]

    sprite_position = range(X - 1, X + 2)
    cycle += 1

print("Part 1:", signal_strength_sum)
print("part 2:")
for line in CRT:
    print("".join(line))
