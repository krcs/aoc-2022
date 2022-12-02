#!/usr/bin/python3

#
# Advent of Code 2022
# Day 2, part 1
# https://github.com/krcs/aoc-2022
#

input = "./input.txt"

def read_lines(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append(line.strip().split(' '))

            if not line:
                break
    return result

lines = read_lines(input)

# Rock defeats Scissors, 
# Scissors defeats Paper, 
# Paper defeats Rock.

player = { 
    'X': 0, # Rock
    'Y': 1, # Paper
    'Z': 2  # Scissor
}

opponent = { 
    'A': 0, # Rock
    'B': 1, # Paper
    'C': 2  # Scissor
}

# column - player
# row - opponent

#       RPS
#       XYZ
#      +---
#  R(A)|360
#  P(B)|036
#  S(C)|603

score_table = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
]

score = 0

for round in lines:
    o = round[0]
    p = round[1]

    score = score + player[p]+1 + score_table[opponent[o]][player[p]]

print(score)
