#!/usr/bin/python3
#
# Advent of Code 2022
# Day 3, part 2
# https://github.com/krcs/aoc-2022
#

import numpy as np
from functools import reduce

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

a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

def sum_priorities(items): 
    result = 0
    for item in items:
        i = ord(item)
        if a <= i <= z:
            result = result + i - 96
        elif A <= i <= Z:
            result = result + i - 38
    return result

result = 0
groups = []

for idx in range(0,len(lines)):
    groups.append(list(lines[idx]))

    if idx%3!=2:
        continue

    items = reduce(np.intersect1d, (groups[0], groups[1], groups[2]))

    result = result + sum_priorities(items)

    groups=[]

print(result)
