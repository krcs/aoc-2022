#!/opt/node/bin/node
/*
    Advent of Code 2022
    Day 10, part 1 and 2
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.trim().split('\n');

function make_move(h, t) {
    const dy = h['y'] - t['y'];
    const dx = h['x'] - t['x'];

    if  (Math.abs(dy) > 1 || Math.abs(dx) > 1) {
        if (dy > 0)
            t['y']++;

        if (dy < 0)
            t['y']--;

        if (dx < 0)
            t['x']--;

        if (dx > 0)
            t['x']++;
    }
}

function get_number_of_unique_tail_positions(rope) {
    let tail_positions = new Set();

    for (let line of lines) {
        const splited = line.split(' ')
        const move = [ splited[0], parseInt(splited[1]) ];

        for (let step = 1; step <= move[1]; step++) {
            const direction = move[0];

            switch (move[0]) {
                case 'U':
                    rope[0]['y']++;
                    break;
                case 'D':
                    rope[0]['y']--;
                    break;
                case 'L':
                    rope[0]['x']--;
                    break;
                case 'R':
                    rope[0]['x']++;
                    break;
            }

            for (let k = 0; k < rope.length-1; k++) {
                make_move(rope[k], rope[k+1]);

                tail_positions.add(JSON.stringify(rope[rope.length-1]));
            }
        }
    }
    return tail_positions.size;
}

function create_rope(length) {
    result = [];
    for (let k = 0; k < length; k++) 
        result.push({ 'x':0, 'y': 0 });
    return result;
}

console.log("Part 1:",get_number_of_unique_tail_positions(create_rope(2)));
console.log("Part 2:",get_number_of_unique_tail_positions(create_rope(10)));
