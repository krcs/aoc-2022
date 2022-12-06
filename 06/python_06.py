#!/usr/bin/python3
#
# Advent of Code 2022
# Day 6, part 1 and 2
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

def find_message(signal, packet_size):
    for idx in range(len(signal)-packet_size+1):
        packet = signal[idx:idx+packet_size]
        if len(set(packet))==len(packet):
            return idx+packet_size

print("Part1:",find_message(lines[0], 4))
print("Part2:",find_message(lines[0], 14))
