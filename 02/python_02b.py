#!/usr/bin/python3
#
# Advent of Code 2022
# Day 2, part 2
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

# X means you need to lose, 
# Y means you need to end the round in a draw, 
# Z means you need to win.

#   XYZ       XYZ      XYZ
#  +---      +---     +---
# R|SRP     R|ZXY    R|201
# P|RPS ->  P|XYZ -> P|012
# S|PSR     S|YZR    S|120

strategy_table = [
    [2,0,1],
    [0,1,2],
    [1,2,0]
]

score = 0

for round in lines:
    o = round[0]
    s = round[1]

    p = strategy_table[opponent[o]][player[s]]
    score = score + p + 1 + score_table[opponent[o]][p]

print(score)
