#!/usr/bin/python3
#
# Advent of Code 2022
# Day 8, part 1
# https://github.com/krcs/aoc-2022
#
input = "./input.txt"

def read_lines(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append([*line.strip()])

            if not line:
                break
    return result

lines = read_lines(input)

rows_count = len(lines)
cols_count = len(lines[0])

visible_count = 0

for r in range(rows_count):
    for c in range(cols_count):
        idx = 1
        top_idx, bottom_idx, left_idx, right_idx = r,r,c,c

        top_visible = True
        top_edge = False

        bottom_visible = True
        bottom_edge = False

        left_visible = True
        left_edge = False

        right_visible = True
        right_edge = False

        while True:
            # TOP
            if top_idx > 0:
                top_idx -= 1
            else:
                top_edge = True

            if not top_edge:
                if lines[top_idx][c] >= lines[r][c]:
                    top_visible = False
                    top_edge = True

            # BOTTOM
            if bottom_idx < rows_count-1:
                bottom_idx += 1
            else:
                bottom_edge = True

            if not bottom_edge:
                if lines[bottom_idx][c] >= lines[r][c]:
                    bottom_visible = False
                    bottom_edge = True

            # LEFT
            if left_idx > 0:
                left_idx -= 1
            else:
                left_edge = True

            if not left_edge:
                if lines[r][left_idx] >= lines[r][c]:
                    left_visible = False
                    left_edge = True

            # RIGHT
            if right_idx < cols_count-1:
                right_idx += 1
            else:
                right_edge = True

            if not right_edge:
                if lines[r][right_idx] >= lines[r][c]:
                    right_visible = False
                    right_edge = True

            if top_edge and bottom_edge and left_edge and right_edge:
                break

        if not any([top_visible, bottom_visible, left_visible, right_visible]):
            visible_count += 1

print("Part1:",rows_count*cols_count-visible_count)
