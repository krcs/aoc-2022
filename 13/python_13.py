#!/usr/bin/python3
#
# Advent of Code 2022
# Day 13, part 1
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
           break

    #if result == None:
    #    print(result, len(left),len(right))

    return result

pairs = []
pair = []

for line in lines:
    if not line:
        pairs.append(pair)
        pair = []
    else: 
        pair.append(eval(line))

pairs.append(pair)

for idx, pair in enumerate(pairs):
    c = compare(pair[0], pair[1])
    print(f"Pair [{idx}]:  {pair} - {c}")

#pair = pairs[3]
#print(f"Result: {compare(pair[0], pair[1])}")
#
