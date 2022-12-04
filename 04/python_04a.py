#!/usr/bin/python3
#
# Advent of Code 2022
# Day 4, part 1
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

is_full_overlap = lambda s1,e1,s2,e2: (s1>=s2 and e1<=e2) or (s2>=s1 and e2<=e1)
get_range_pair_from_str = lambda s: list(map(int,s.split('-')))

result = 0

for line in lines:
    pair_range = line.split(',')
    p1 = get_range_pair_from_str(pair_range[0])
    p2 = get_range_pair_from_str(pair_range[1])

    if is_full_overlap(p1[0],p1[1],p2[0],p2[1]):
        result += 1

print(result)
