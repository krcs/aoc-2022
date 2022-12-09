#!/usr/bin/python3
#
# Advent of Code 2022
# Day 9, part 1
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

h = { 'x': 0, 'y': 0 }
t = { 'x': 0, 'y': 0 }

tail_positions = [ [0,0] ]

def add_position(p, positions):
    pos = [ p['x'], p['y'] ]
    if not pos in positions:
        positions.append(pos)

for line in lines:
    splited = line.split(' ')
    move = [ splited[0], int(splited[1]) ]
    for step in range(1,move[1]+1):
        direction = move[0]

        if direction == 'U':
            h['y'] += 1
            if abs(h['y']-t['y']) > 1 or abs(t['x']-h['x']) > 1:
                t['y'] = h['y']-1
                t['x'] = h['x']

                add_position(t, tail_positions)

        elif direction == 'D':
            h['y'] -= 1
            if abs(h['y']-t['y']) > 1 or abs(t['x']-h['x']) > 1:
                t['y'] = h['y']+1
                t['x'] = h['x']

                add_position(t, tail_positions)

        elif direction == 'L':
            h['x'] -= 1
            if abs(h['y']-t['y']) > 1 or abs(t['x']-h['x']) > 1:
                t['y'] = h['y']
                t['x'] = h['x']+1

                add_position(t, tail_positions)

        elif direction == 'R':
            h['x'] += 1
            if abs(h['y']-t['y']) > 1 or abs(t['x']-h['x']) > 1:
                t['y'] = h['y']
                t['x'] = h['x']-1

                add_position(t, tail_positions)

    #print(f"{_idx}: Move: {move}, h: {h}, t: {t}")

print("Part 1:",len(tail_positions))
