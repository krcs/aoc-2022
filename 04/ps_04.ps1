#
# Advent of Code 2022
# Day 4, part 1 and 2
# https://github.com/krcs/aoc-2022
#
$part1 = 0
$part2 = 0
cat './input.txt' | ? {
    $pairs = $_.split(',')
    $p1 = $pairs[0].split('-')
    $p2 = $pairs[1].split('-')
    if (([int]$p1[0] -ge [int]$p2[0] -and [int]$p1[1] -le [int]$p2[1]) -or
        ([int]$p2[0] -ge [int]$p1[0] -and [int]$p2[1] -le [int]$p1[1])) {
            $part1 += 1
    }
    if ([int]$p1[0] -le [int]$p2[1] -and [int]$p1[1] -ge [int]$p2[0]) {
        $part2 += 1
    }
} 
write-host "Part1: $part1"
write-host "Part2: $part2"
