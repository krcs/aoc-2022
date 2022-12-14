#!/usr/bin/python3
#
# Advent of Code 2022
# Day 14, part 1
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

def print_board(board): 
    for ridx in range(len(board)):
        print(f"{ridx:3} ", end="")
        for cidx in range(len(board[0])):
            print(board[ridx][cidx], end="")
        print()

def generate_board(lines):
    board = []

    rock_lines = []
    minX, maxX = -1, 0
    minY, maxY = -1, 0

    line_points = []

    for line in lines:
        points_str = line.split(' -> ')
        points = []
        for point_str in points_str:
            point_spl = point_str.split(',')
            point = {
                'x': int(point_spl[0]),
                'y': int(point_spl[1])
            }
            if point['x'] > maxX:
                maxX = point['x']

            if point['x'] < minX or minX == -1:
                minX = point['x']
            
            if point['y'] > maxY:
                maxY = point['y']

            if point['y'] < minY or minY == -1:
                minY = point['y']
            points.append(point)
        line_points.append(points)

    for ridx in range(0, maxY+1):
        row = []
        for cidx in range(minX, maxX+1):
            row.append('.')
        board.append(row)

    for pl in line_points:
        for point in range(len(pl)-1):
            p1 = pl[point]
            p2 = pl[point+1]
            s1_x, s2_x = sorted([p1['x']-minX, p2['x']-minX])
            s1_y, s2_y = sorted([p1['y'], p2['y']])
            for y in range(s1_y, s2_y+1):
                for x in range(s1_x, s2_x+1):
                    board[y][x] = '#'
    return board, { 
        'minX': minX, 
        'minY': 0,
        'maxX': maxX,
        'maxY': maxY
    }

def move(current_pos, x, y, board):
    board[current_pos['y']][current_pos['x']] = '.'
    current_pos['x'] = x
    current_pos['y'] = y
    board[current_pos['y']][current_pos['x']] = 'o'

lines = read_lines(input)

board, edges = generate_board(lines)

HEIGHT = len(board)
WIDTH = len(board[0])

start_pos = { 
    'x': 500 - edges['minX'],
    'y': 0 - edges['minY']
}

pos = start_pos.copy()
csand = 1

while True:
    x = pos['x']
    y = pos['y'] + 1

    if y < HEIGHT:
        if board[y][x] == '.':
            move(pos, x, y, board)
            continue

        if x-1 >= 0:
            if board[y][x-1] == '.':
                move(pos, x-1, y, board)
                continue
        else:
            break

        if x+1 < WIDTH:
            if board[y][x+1] == '.':
                move(pos, x+1, y, board)
                continue
            pos = start_pos.copy()
            csand += 1
        else:
            break
    else:
        break

print("Part 1:", csand-1)
