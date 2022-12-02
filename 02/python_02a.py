#!/usr/bin/python3
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

# A - Rock
# B - Paper
# C - Scissor

# X - Rock
# Y - Paper
# Z - Scissor

# Rock defeats Scissors, 
# Scissors defeats Paper, 
# Paper defeats Rock.

for round in lines:
    round_score = 0
    opponent = round[0]
    player = round[1]
    if player == 'X':
        round_score=1
    elif player == 'Y':
        round_score=2
    elif player == 'Z':
        round_score=3

    print(round,round_score)

