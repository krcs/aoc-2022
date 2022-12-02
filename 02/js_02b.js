/*
    Advent of Code 2022
    Day 1, part 2
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.trim().split('\r\n');

player = {
    'X': 0,
    'Y': 1,
    'Z': 2
}

opponent = {
    'A': 0,
    'B': 1,
    'C': 2
}

score_table = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
];

strategy_table = [
    [2,0,1],
    [0,1,2],
    [1,2,0]
];

score = 0;

for (let line of lines) {
    let r = line.split(' ');
    let o = r[0];
    let s = r[1];

    p = strategy_table[opponent[o]][player[s]]
    score = score + p + 1 + score_table[opponent[o]][p]
}
console.log(score);
