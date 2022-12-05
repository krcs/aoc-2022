#!/usr/bin/python3
#
# Advent of Code 2022
# Day 5, part 1
# https://github.com/krcs/aoc-2022
#
import re

input = "./input.txt"

def get_stacks_and_moves(filename):
    stacks = []
    moves = []

    is_moves_section = False

    with open(filename,'r') as f:
        stacks_lines=[]
        while True:
            line = f.readline()
            if not line:
                break

            line = line.replace('\n','')

            if len(line.strip())==0:
                is_moves_section = True

                number_of_stacks = max(map(int,re.findall('\d+',stacks_lines[-1])))
                stacks = [ [] for n in range(number_of_stacks) ]
                for stack_str in reversed(stacks_lines[:-1]):
                    sidx = 0
                    for ci in range(len(stack_str)):
                        if ci%4 == 1:
                            if stack_str[ci]!=' ':
                                stacks[sidx].append(stack_str[ci])
                            sidx+=1
                continue

            if not is_moves_section:
                stacks_lines.append(line)
            else:
                move_str = line.split(' ')
                move = {
                    'move': int(move_str[1]),
                    'from': int(move_str[3]),
                      'to': int(move_str[5])
                }
                moves.append(move)
    return stacks,moves

def print_stacks(stacks):
    for idx,crate in enumerate(stacks):
        print(idx+1, crate)

def get_tops_crates(stacks):
    return ''.join([ stack[-1] for stack in stacks ])

stacks, moves = get_stacks_and_moves(input)

#print_stacks(stacks)
#print()
for move in moves:
    #print(move)
    for n in range(move['move']):
        stacks[move['to']-1].append(stacks[move['from']-1].pop())
    #print_stacks(stacks)
    #print()

print(get_tops_crates(stacks))
