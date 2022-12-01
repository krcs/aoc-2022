#!/usr/bin/python3
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

elfs = []
calories = []

lines = read_lines(input)

for line in lines:
    if len(line)==0:
        elfs.append(sum(calories))
        calories = []
        continue

    calories.append(int(line))

print(max(elfs))
