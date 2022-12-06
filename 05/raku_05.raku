#
# Advent of Code 2022
# Day 5, part 1 and 2
# https://github.com/krcs/aoc-2022
#
my $is_moves_section = False;
my @moves = ();
my @stacks = ();

for './input.txt'.IO.lines -> $line {
    when $line.chars == 0 {
        $is_moves_section = True;
        next;
    }
    when (!$is_moves_section) {
        my $ri = 0;
        for 0..$line.chars -> $si {
            if ($si % 4 == 1) {
                my $c = $line.comb[$si];
                if ($c ne ' ') {
                    @stacks[$ri].unshift($c);
                }
                $ri++;
            }
        }
    }
    when ($is_moves_section) {
        my $move = $line.split(' ');
        @moves.push({
            'move' => +$move[1],
            'from' => +$move[3],
              'to' => +$move[5]
        });
    }
}

sub get_tops_from_stacks(@stacks) {
    my $result = '';
    for @stacks -> @stack {
        if (@stack.elems gt 1) {
            $result ~= @stack.tail;
        }
    }
    $result;
}

sub clone_array(@source) {
    my @result;
    for @source -> @elem {
        @result.push(@elem.clone);
    }
    @result;
}

my @part1_stacks = @stacks;
my @part2_stacks = clone_array(@stacks);

for @moves -> %move {
    my $moves = %move<move>;
    my $from = %move<from>-1;
    my $to = %move<to>-1;

    my $shift = @part2_stacks[$from].elems-$moves;
    for 0..$moves-1 -> $m {
        @part1_stacks[$to].push(@part1_stacks[$from].pop());
    }
    @part2_stacks[$to].append(@part2_stacks[$from].splice($shift, $moves));
}
say "Part1: {get_tops_from_stacks @part1_stacks}";
say "Part2: {get_tops_from_stacks @part2_stacks}";
