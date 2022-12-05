#!/opt/node/bin/node
/*
    Advent of Code 2022
    Day 5, part 1 and 2
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.split('\n');

let is_moves_section = false;

const stacks = [];
const moves = [];

for (let line of lines) {
    if (line.length === 0) {
        is_moves_section = true;
        continue;
    }

    if (!is_moves_section) {
        let ridx = 0;
        for (let sidx in line) {
            if (sidx % 4 === 1) {
                if (stacks.length < ridx+1) 
                    stacks.push([])
                if (line[sidx]!=' ')
                    stacks[ridx].unshift(line[sidx])
                ridx++;
            }
        }
    }

    if (is_moves_section) {
        move = line.split(' ');
        moves.push({
            'move': parseInt(move[1]),
            'from': parseInt(move[3]),
              'to': parseInt(move[5])
        });
    }
}

function get_tops_from_stacks(stacks) {
    let result = '';
    for (let stack of stacks)
        if (stack.length>1)
            result+=stack[stack.length-1]
    return result;
}

const part1_stacks = stacks;
const part2_stacks = JSON.parse(JSON.stringify(stacks));

for (let move of moves) {
    let moves = move['move'];
    let from = move['from']-1;
    let to = move['to']-1;
    let shift = part2_stacks[from].length-moves;

    for (let m=0; m<moves;++m)
        part1_stacks[to].push(part1_stacks[from].pop());

    part2_stacks[to] = part2_stacks[to]
        .concat(part2_stacks[from].splice(shift,moves))
}

console.log("Part1:",get_tops_from_stacks(part1_stacks));
console.log("Part2:",get_tops_from_stacks(part2_stacks));
