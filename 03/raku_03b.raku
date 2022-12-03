#
# Advent of Code 2022
# Day 3, part 2
# https://github.com/krcs/aoc-2022
#

my $result = 0;
my $idx = 0;
my @group;

for './input.txt'.IO.lines -> $line {
    @group.push: $line.split("",:skip-empty);

    if ($idx mod 3) eq 2 {
        for (@group[0] (&) @group[1] (&) @group[2]).keys -> $item {
            $result += $item.ord-96 if $item (elem) 'a'..'z';
            $result += $item.ord-38 if $item (elem) 'A'..'Z';
        }
        @group = ()
    };
    $idx++;
}
say $result
