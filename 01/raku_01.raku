#
# Advent of Code 2022
# Day 1, part 1 and 2
# https://github.com/krcs/aoc-2022
#
my $sum = 0;
my @sums = ();

for './input.txt'.IO.lines -> $line {
    if $line.chars == 0 {
        @sums.push($sum);
        $sum = 0;
    }
    $sum += $line;
}
say "Part1: {@sums.max}";
say "Part2: {@sums.sort.tail(3).sum}";
