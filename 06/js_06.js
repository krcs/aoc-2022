#!/opt/node/bin/node
/*
    Advent of Code 2022
    Day 6, part 1 and 2
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.trim().split('\n');

function is_unique(packet) {
    if (packet.length<=1)
        return true;

    for (let i=0; i < packet.length-1;++i)
        for (let j=i+1; j < packet.length;++j)
            if (packet[i]===packet[j])
                return false;
    return true;
}

function find_message(signal, packet_size) {
    for (let idx=0; idx<signal.length-packet_size-1; ++idx) {
        let packet=signal.substring(idx,idx+packet_size);
        if (is_unique(packet))
            return idx+packet_size;
    }
    return -1;
}

console.log("Part1:", find_message(lines[0],4));
console.log("Part2:", find_message(lines[0],14));
