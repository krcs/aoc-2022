#!/usr/bin/python3
#
# Advent of Code 2022
# Day 12, part 1 and 2
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

WEIGHT = { chr(a): a-97 for a in range(ord('a'), ord('z')+1) }
WEIGHT['S'] = WEIGHT['a']
WEIGHT['E'] = WEIGHT['z']

offsets = [ (1,0), (-1,0), (0,1), (0, -1) ]

def get_pos_of_char(char, grid):
    result = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == char:
                result.append((row, col))
    return result

def bfs(start_position, grid):
    queue = [ (start_position, 0) ]
    visited = set(start_position)
    GRID_WIDTH = len(grid[0])
    GRID_HEIGHT = len(grid)

    while queue:
        (r, c), count = queue.pop(0)
        current_value = grid[r][c]

        if  current_value == 'E':
            return count

        for ro, co in offsets:
            next_move = (r + ro, c + co)

            if next_move in visited:
                continue

            if next_move[0] < 0 or next_move[0] >= GRID_HEIGHT \
                or next_move[1] < 0 or next_move[1] >= GRID_WIDTH:
                continue

            next_value = grid[next_move[0]][next_move[1]]

            if WEIGHT[next_value] <= WEIGHT[current_value] + 1:
                visited.add(next_move)
                queue.append((next_move, count + 1))
    return -1

lines = read_lines(input)

grid = []
for line in lines:
    grid.append([*line])

start_positions = get_pos_of_char('S', grid)

part1 = bfs(start_positions[0], grid)
print("Part 1:", part1)

part2 = 0
start_positions = get_pos_of_char('a', grid)
for pos in start_positions:
    count = bfs(pos, grid)
    if count < 0:
        continue

    if part2 == 0 or count < part2:
        part2 = count

print("Part 2:", part2)
