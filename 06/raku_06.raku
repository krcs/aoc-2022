#
# Advent of Code 2022
# Day 6, part 1 and 2
# https://github.com/krcs/aoc-2022
#

sub find_message($signal, $packet_size) {
    my $result = 0;
    for 0..$signal.chars-$packet_size -> $idx {
        my $packet = $signal.substr($idx..$idx+$packet_size-1);
        my $count_unique = $packet.split("", :skip-empty).unique.elems;
        if $count_unique == $packet.chars {
            $result = $idx+$packet_size;
            last;
        }
    }
    $result;
}

my @lines = './input.txt'.IO.lines;

say "Part1: {find_message(@lines[0], 4)}";
say "Part2: {find_message(@lines[0], 14)}";
