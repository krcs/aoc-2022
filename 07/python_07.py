#!/usr/bin/python3
#
# Advent of Code 2022
# Day 7, part 1
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

le100000 = lambda size : size if size < 100000 else 0

def get_tree(current_folder, idx, lines, result):
    sum_size = 0
    while idx < len(lines):
        if lines[idx].startswith('$'):
            cmd, *args = lines[idx].split(' ')[1:]

            if cmd == 'cd':
                if args:
                    arg = args[0]
                else:
                    pass

                if arg == '..':
                    current_folder['size'] = sum_size
                    result.append(le100000(sum_size))
                    return current_folder, idx;
                else:
                    current_folder[arg], idx = get_tree(current_folder[arg], idx+1, lines, result)
                    sum_size += current_folder[arg]['size']

            if cmd == 'ls':
                pass

        elif lines[idx].startswith('dir'):
            name = lines[idx].split(' ')[1]
            current_folder[name] = {}
        else:
            file_row=lines[idx].split(' ')
            name = file_row[1]
            size = int(file_row[0])
            current_folder[name] = size;
            sum_size += size

        idx+=1
    current_folder['size'] = sum_size
    result.append(le100000(sum_size))
    return current_folder, idx

result = []
tree, _ = get_tree({ '/' : {} }, 0, lines, result)

print("Part1:",sum(result))
