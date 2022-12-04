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

result = 0

for line in lines:
    pair_range = line.split(',')
    p1 = list(map(int,pair_range[0].split('-')))
    p2 = list(map(int,pair_range[1].split('-')))
    overlap = (p1[0]>=p2[0] and p1[1]<=p2[1]) or (p2[0]>=p1[0] and p2[1]<=p1[1])
    if overlap:
        result += 1

print(result)
