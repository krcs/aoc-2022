#!/usr/bin/python3
#
# Advent of Code 2022
# Day 13, part 1 and 2
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

def compare(left, right):
    if type(left)==list and type(right)==list:
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(left) > 0 and len(right) == 0:
            return False

    elif type(left)==int and type(right)==int:
        if left != right:
            return left < right
        else:
            return None

    elif type(left)==int and type(right)==list:
        return compare([left], right)

    elif type(left)==list and type(right)==int:
        return compare(left, [right])

    n = len(left) if len(left) < len(right) else len(right)

    result = None

    for idx in range(n):
       result = compare(left[idx], right[idx])
       if result != None:
           return result

    if result == None and len(left) != len(right):
        return len(left) < len(right)

def get_pairs(lines):
    pairs = []
    pair = []
    for line in lines:
        if not line:
            pairs.append(pair)
            pair = []
        else: 
            pair.append(eval(line))
    pairs.append(pair)
    return pairs

def part2(packets):
    p1,p2 = packets[-2:]

    result = 1

    for i in range(0, len(packets)-1):
        for j in range(i+1, len(packets)):
            if not compare(packets[i], packets[j]):
                packets[i], packets[j] = packets[j], packets[i]
        if packets[i] == p1 or packets[i] == p2:
            result *= i+1

    return result

pairs = get_pairs(lines)

part1 = 0
for idx, pair in enumerate(pairs):
    if compare(pair[0], pair[1]):
        part1 += idx + 1

print("Part 1:", part1)

part2 = part2(sum(pairs,[])+[ [[2]], [[6]] ])

print("Part 2:", part2)
