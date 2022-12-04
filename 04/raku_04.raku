#
# Advent of Code 2022
# Day 4, part 1 and 2
# https://github.com/krcs/aoc-2022
#
my $part1 = 0;
my $part2 = 0;

for './input.txt'.IO.lines -> $line {
    my $pairs = $line.split(",", :skip-empty);
    my $p1 = $pairs[0].split("-", :skip-empty);
    my $p2 = $pairs[1].split("-", :skip-empty);
    if (($p1[0] >= $p2[0] and $p1[1] <= $p2[1]) or 
        ($p2[0] >= $p1[0] and $p2[1] <= $p1[1])) {
            $part1++
    }
    if ($p1[0] <= $p2[1] and $p1[1] >= $p2[0]) {
        $part2++;
    }
}
say "Part1: $part1";
say "Part2: $part2";
