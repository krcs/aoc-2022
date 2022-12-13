#!/usr/bin/python3
#
# Advent of Code 2022
# Day 13, part 1
# https://github.com/krcs/aoc-2022
#
input = "./test.txt"

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

for line in lines:
    if not line:
        continue
    print(eval(line))
    
