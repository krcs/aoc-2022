#!/usr/bin/python3
#
# Advent of Code 2022
# Day 4, part 1 and 2
# https://github.com/krcs/aoc-2022
#
import numpy as np

input = "./input.txt"

is_full_overlap = \
    lambda pair: (pair[0][0]>=pair[1][0] and pair[0][1]<=pair[1][1]) or \
                 (pair[1][0]>=pair[0][0] and pair[1][1]<=pair[0][1])

is_overlap = \
    lambda pair: pair[0][0]<=pair[1][1] and pair[0][1] >= pair[1][0]

pairs = np.loadtxt(input, \
        delimiter=',', \
        dtype=int, \
        encoding="ascii",\
        converters={ 
            i: lambda r: r.split("-") for i in range(2) 
        })

print("Part1:",sum(list(map(is_full_overlap,pairs))))
print("Part2:",sum(list(map(is_overlap,pairs))))
