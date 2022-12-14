#!/opt/node/bin/node
/*
    Advent of Code 2022
    Day 7, part 1 and 2
    https://github.com/krcs/aoc-2022
*/
const fs = require('fs');

const lines = fs.readFileSync('./input.txt', 'UTF-8').trim().split('\n');

const is_less_equal_100k = (size) => size < 100000 ? size : 0;

function get_tree(current_folder, idx, lines, le100k) {
    let sum_size = 0;

    while (idx < lines.length) {
        const line = lines[idx].split(' ');

        if (line[0] === '$') {
            const cmd = line[1];
            const arg = line.length > 2 ? line[2] : "";

            if (cmd === "cd") {
                if (arg == '..') {
                    current_folder['size'] = sum_size;

                    le100k.push(is_less_equal_100k(sum_size));

                    return [ current_folder, idx ];
                } else {
                    [ current_folder[arg] , idx ] = get_tree(current_folder[arg], idx+1, lines, le100k);
                    sum_size += current_folder[arg]['size'];
                }
            }
        } else if (lines[idx].startsWith('dir')) {
            const [ _, name  ] = lines[idx].split(' ');
            current_folder[name] = {};
        } else {
            const [ size, name ] = lines[idx].split(' ');
            current_folder[name] = parseInt(size);
            sum_size += current_folder[name];
        }
        idx++;
    }
    current_folder['size'] = sum_size;

    le100k.push(is_less_equal_100k(sum_size));

    return [ current_folder, idx ]
}

function get_size_of_directory_to_delete(tree, min_space_to_free, result) {
    for (let key in tree) {
        if (typeof tree[key] === 'object') {
            if (tree[key]['size'] >= min_space_to_free &&
                tree[key]['size'] < result[0])
                result[0] = tree[key]['size'];
            get_size_of_directory_to_delete(tree[key], min_space_to_free, result);
        }
    }
}

let part1 = [];
const [ tree, _ ] = get_tree({ '/' : {} }, 0, lines, part1);

console.log("Part 1:", eval(part1.join('+')));

const total_disk_size = 70_000_000;
const required_size = 30_000_000;
const used_space = tree['/']['size'];
const current_free_space = total_disk_size-used_space;
const min_space_to_free = required_size-current_free_space;

result = [used_space];
get_size_of_directory_to_delete(tree, min_space_to_free, result);

console.log("Part 2:", result[0]);
