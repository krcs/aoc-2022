#!/usr/bin/python3
#
# Advent of Code 2022
# Day 10, part 1
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

while True:

    if not instruction:

        if instruction_pointer >= len(lines): 
            break
        
        instruction, *arg = lines[instruction_pointer].split(' ')

        if instruction == 'noop':
            end_execution_cycle = cycle

        elif instruction == 'addx':
            end_execution_cycle = cycle + 1
            if arg:
                V = int(arg[0])

        instruction_pointer += 1

    #print(f"Cycle:[{cycle}] - X={X}, I={instruction if instruction else '---'} V={V if V else '---'} EEC={end_execution_cycle} IP={instruction_pointer}")

    if (cycle + 20) % 40 == 0 and cycle <= 220:
        signal_strength_sum += cycle * X

    if cycle == end_execution_cycle:
        if instruction == 'addx':
            X += V
        end_execution_cycle = 0
        instruction, V  = [ None, None ]

    cycle += 1

print("Part 1:", signal_strength_sum)
