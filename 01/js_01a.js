/*
    Advent of Code 2022
    Day 1, part 1
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.split('\r\n');

let sum = 0;
let max = 0;

for (let line of lines) {
    if (line.length === 0) {
        if (sum > max) 
            max = sum;
        sum=0;
    } else
        sum += parseInt(line);
}

console.log(max)
