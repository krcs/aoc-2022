#!/usr/bin/python3
elfs = []
calories = []

f = open("./input.txt","r")
while True:
    line = f.readline()

    if not line:
        break

    if line == '\n':
        elfs.append(sum(calories))
        calories = []
        continue

    calories.append(int(line))

f.close()
s=sorted(elfs,reverse=True)
print(sum([s[0],s[1],s[2]]))
