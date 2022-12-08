#!/usr/bin/python3
#
# Advent of Code 2022
# Day 8, part 1 and 2
# https://github.com/krcs/aoc-2022
#
input = "./input.txt"

def read_trees(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append([*line.strip()])

            if not line:
                break
    return result

trees = read_trees(input)

rows_count = len(trees)
cols_count = len(trees[0])

best_distance = 0
visible_count = 0

for r in range(rows_count):
    for c in range(cols_count):
        idx = 1
        top_idx, bottom_idx, left_idx, right_idx = r,r,c,c

        top_visible = True
        top_edge = False
        top_distance = 0

        bottom_visible = True
        bottom_edge = False
        bottom_distance = 0

        left_visible = True
        left_edge = False
        left_distance = 0

        right_visible = True
        right_edge = False
        right_distance = 0

        distance = 0

        while True:
            # TOP
            if top_idx > 0:
                top_idx -= 1
            else:
                top_edge = True

            if not top_edge:
                if trees[top_idx][c] >= trees[r][c]:
                    top_visible = False
                    top_edge = True

                top_distance += 1

            # BOTTOM
            if bottom_idx < rows_count-1:
                bottom_idx += 1
            else:
                bottom_edge = True

            if not bottom_edge:
                if trees[bottom_idx][c] >= trees[r][c]:
                    bottom_visible = False
                    bottom_edge = True

                bottom_distance += 1

            # LEFT
            if left_idx > 0:
                left_idx -= 1
            else:
                left_edge = True

            if not left_edge:
                if trees[r][left_idx] >= trees[r][c]:
                    left_visible = False
                    left_edge = True

                left_distance += 1

            # RIGHT
            if right_idx < cols_count-1:
                right_idx += 1
            else:
                right_edge = True

            if not right_edge:
                if trees[r][right_idx] >= trees[r][c]:
                    right_visible = False
                    right_edge = True

                right_distance += 1

            if top_edge and bottom_edge and left_edge and right_edge:
                break

        if not any([top_visible, bottom_visible, left_visible, right_visible]):
            visible_count += 1

        distance = top_distance*bottom_distance*left_distance*right_distance
        if distance > best_distance:
            best_distance = distance

print("Part 1:",rows_count*cols_count-visible_count)
print("Part 2:",best_distance)
