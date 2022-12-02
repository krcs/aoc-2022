/*
    Advent of Code 2022
    Day 1, part 1
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
]

score = 0;

for (let line of lines) {
    let r = line.split(' ');
    let o = r[0];
    let p = r[1];

    score = score + player[p]+1 + score_table[opponent[o]][player[p]]
}
console.log(score);
