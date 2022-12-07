#!/usr/bin/python3
#
# Advent of Code 2022
# Day 7, part 2
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

def get_tree(current_folder, idx, lines):
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
                    return current_folder, idx;
                else:
                    current_folder[arg], idx = get_tree(current_folder[arg], idx+1, lines)
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
    return current_folder, idx

def get_size_of_directory_to_delete(tree, min_space_to_free, result):
    for key in tree:
        if type(tree[key]) is dict:
            if tree[key]['size'] >= min_space_to_free \
                    and tree[key]['size'] < result[0]:
               result[0]=tree[key]['size']
            get_size_of_directory_to_delete(tree[key], min_space_to_free, result)

tree, _ = get_tree({ '/' : {} }, 0, lines)

total_disk_size = 70_000_000
required_size = 30_000_000
used_space = tree['/']['size']
current_free_space = total_disk_size-used_space
min_space_to_free = required_size-current_free_space

result = [used_space]

get_size_of_directory_to_delete(tree, min_space_to_free, result)

print("Part 2:",result[0])

