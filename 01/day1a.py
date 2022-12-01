#!/usr/bin/python3
input = "./input.txt"

elfs = []
calories = []

with open(input,'r') as f:
    while True:
        line = f.read().strip()

        if not line:
            break

        if line!="\n":
            print(line,len(line))
            #calories.append(int(line))
        #elif len(line)==0:
        #    elfs.append(sum(calories))
       #     calories = []


#print(max(elfs))
