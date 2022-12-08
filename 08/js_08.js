#!/opt/node/bin/node
/*
    Advent of Code 2022
    Day 8, part 1 and 2
    https://github.com/krcs/aoc-2022
*/

const fs = require('fs');

const lines = fs.readFileSync('./input.txt', 'UTF-8')

const trees = lines.trim().split('\n');

const rows_count = trees.length;
const cols_count = trees[0].length;

let best_distance = 0;
let visible_count = 0;

for (let r = 0; r < rows_count; ++r)
    for (let c = 0; c < cols_count; ++c) {
        let top_idx=r, bottom_idx=r, left_idx=c, right_idx=c;

        let top_visible = true;
        let top_edge = false;
        let top_distance = 0;

        let bottom_visible = true;
        let bottom_edge = false;
        let bottom_distance = 0;

        let left_visible = true;
        let left_edge = false;
        let left_distance = 0;

        let right_visible = true;
        let right_edge = false;
        let right_distance = 0;

        let distance = 0;

        while (true) {
            // TOP
            if (top_idx > 0)
                top_idx -= 1;
            else
                top_edge = true;

            if (!top_edge) {
                if (trees[top_idx][c] >= trees[r][c]) {
                    top_visible = false;
                    top_edge = true;
                }
                top_distance++;
            }

            // BOTTOM 
            if (bottom_idx < rows_count-1)
                bottom_idx += 1;
            else
                bottom_edge = true;

            if (!bottom_edge) {
                if (trees[bottom_idx][c] >= trees[r][c]) {
                    bottom_visible = false;
                    bottom_edge = true;
                }
                bottom_distance++;
            }

            // LEFT
            if (left_idx > 0)
                left_idx -= 1;
            else
                left_edge = true;

            if (!left_edge) {
                if (trees[r][left_idx] >= trees[r][c]) {
                    left_visible = false;
                    left_edge = true;
                }
                left_distance++;
            }

            // right
            if (right_idx < cols_count-1)
                right_idx += 1;
            else
                right_edge = true;

            if (!right_edge) {
                if (trees[r][right_idx] >= trees[r][c]) {
                    right_visible = false;
                    right_edge = true;
                }
                right_distance++;
            }

            if (top_edge && bottom_edge && left_edge && right_edge)
                break;
        }

        if (!(top_visible || bottom_visible || left_visible || right_visible))
            visible_count++;

        distance = top_distance*bottom_distance*left_distance*right_distance;
        if (distance > best_distance)
            best_distance = distance;
    }

console.log("Part 1:",rows_count*cols_count-visible_count)
console.log("Part 2:",best_distance)
