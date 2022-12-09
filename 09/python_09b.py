#!/usr/bin/python3
#
# Advent of Code 2022
# Day 9, part 2
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

rope = [
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 },
    { 'x': 0, 'y': 0 }
]

tail_positions = [ [0,0] ]

def add_position(p, positions):
    pos = [ p['x'], p['y'] ]
    if not pos in positions:
        positions.append(pos)

def make_move(h, t, k):

    dy = h['y'] - t['y']
    dx = h['x'] - t['x']

    direction_x = ''
    direction_y = ''

    if dy > 0:
        direction_y = 'U'
    elif dy < 0:
        direction_y = 'D'

    if dx < 0:
        direction_x = 'L'
    elif dx > 0:
        direction_x = 'R'

    direction = direction_y

    if dx > dy:
        direction = direction_x

    print(f"  h:[{k}] - t:[{k+1}] - {direction}, {h}, {t}, dx:{dx}, dy:{dy}, {direction_x}, {direction_y}")

    if direction == 'U':
        if abs(dy) > 1 or abs(dx) > 1:
            t['y'] = h['y']-1
            t['x'] = h['x']

    elif direction == 'D':
        if abs(dy) > 1 or abs(dx) > 1:
            t['y'] = h['y']+1
            t['x'] = h['x']

    elif direction == 'L':
        if abs(dy) > 1 or abs(dx) > 1:
            t['y'] = h['y']
            t['x'] = h['x']+1

    elif direction == 'R':
        if abs(dy) > 1 or abs(dx) > 1:
            t['y'] = h['y']
            t['x'] = h['x']-1

    print(f"                - {direction}, {h}, {t}, dx:{dx}, dy:{dy}, {direction_x}, {direction_y}")

for line in lines[:2]:
    splited = line.split(' ')
    move = [ splited[0], int(splited[1]) ]

    debug_step_idx = 0

    for step in range(1,move[1]+1):
        direction = move[0]

        if direction == 'U':
            rope[0]['y'] += 1
        elif direction == 'D':
            rope[0]['y'] -= 1
        elif direction == 'L':
            rope[0]['x'] -= 1
        elif direction == 'R':
            rope[0]['x'] += 1

        print(f"[{debug_step_idx}] - step")

        for k in range(len(rope)-1):
            make_move(rope[k], rope[k+1], k)

        debug_step_idx += 1
    debug_k = ""
    for i,k in enumerate(rope):
        debug_k += f"[{i}]:x={k['x']},y={k['y']} "
    print(f"{move} {debug_k}")


