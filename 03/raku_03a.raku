#
# Advent of Code 2022
# Day 3, part 1
# https://github.com/krcs/aoc-2022
#

my $result = 0;
my $lower = list('a'..'z');
my $upper = list('A'..'Z');

for './input.txt'.IO.lines -> $line {
    my $half = $line.chars / 2;
    my $c1 = $line.substr(0..$half-1).split("",:skip-empty);
    my $c2 = $line.substr($half, $half).split("",:skip-empty);

    for ($c1 (&) $c2).keys -> $item {
        $result += $item.ord-96 if $item (elem) $lower;
        $result += $item.ord-38 if $item (elem) $upper;
    }
}
say $result
