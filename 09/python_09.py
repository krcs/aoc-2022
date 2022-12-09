#!/usr/bin/python3
#
# Advent of Code 2022
# Day 9, part 1 and 2
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

def make_move(h, t):

    dy = h['y'] - t['y']
    dx = h['x'] - t['x']

    direction_x = None
    direction_y = None

    if dy > 0:
        direction_y = 'U'
    elif dy < 0:
        direction_y = 'D' 

    if dx < 0: 
        direction_x = 'L' 
    elif dx > 0: 
        direction_x = 'R' 

    if abs(dy) > 1 or abs(dx) > 1:
       if direction_y == 'U':
            t['y'] += 1

       if direction_y == 'D':
            t['y'] -= 1

       if direction_x == 'L':
            t['x'] -= 1

       if direction_x == 'R':
            t['x'] += 1

def get_number_of_unique_tail_position(rope):
    tail_positions = set()

    for line in lines:
        splited = line.split(' ')
        move = [ splited[0], int(splited[1]) ]

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

            for k in range(len(rope)-1):
                make_move(rope[k], rope[k+1])

                tail_positions.add((rope[-1]['x'], rope[-1]['y']))

    return len(tail_positions)

rope_part_1 = [ {'x':0, 'y': 0 } for n in range(2) ]
print("Part 1:", get_number_of_unique_tail_position(rope_part_1))

rope_part_2 = [ {'x':0, 'y': 0 } for n in range(10) ]
print("Part 2:", get_number_of_unique_tail_position(rope_part_2))
