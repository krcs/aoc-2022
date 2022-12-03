#!/usr/bin/python3

#
# Advent of Code 2022
# Day 3, part 2
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

def sum_priorities(items): 
    result = 0
    for item in items:
        i = ord(item)
        if i in range(ord('a'),ord('z')+1):
            result = result + i - 96
        elif i in range(ord('A'),ord('Z')+1):
            result = result + i - 38
    return result


lines = read_lines(input)

result = 0
groups = []

for idx in range(0,len(lines)):
    groups.append(lines[idx])

    if idx%3!=2:
        continue

    items = set(groups[0]).intersection(set(groups[1])).intersection(set(groups[2]))

    result = result + sum_priorities(items)
    groups=[]

print(result)
