#
# Advent of Code 2022
# Day 3, part 1
# https://github.com/krcs/aoc-2022
#

my $result = 0;

for './input.txt'.IO.lines -> $line {
    my $arr = $line.split("", :skipt-empty);
    my $half = $arr.elems / 2;
    my $c1 = $arr[0..$half-1];
    my $c2 = $arr[$half..*];

    for ($c1 (&) $c2).keys -> $item {
        $result += $item.ord-96 if $item (elem) 'a'..'z';
        $result += $item.ord-38 if $item (elem) 'A'..'Z';
    }
}
say $result
