#
# Advent of Code 2022
# Day 3, part 1
# https://github.com/krcs/aoc-2022
#

$result = 0
cat "./input.txt" | % {
    $comparment_1 = $_.substring(0, $_.length/2).ToCharArray()
    $comparment_2 = $_.substring($_.length/2).ToCharArray()

    $comparment_1 | select -unique | ? { $comparment_2 -ccontains $_ } | % {
        $result += ($p=('a'..'z').IndexOf([char]$_)) -ge 0 ? $p + 1  : 0
        $result += ($p=('A'..'Z').IndexOf([char]$_)) -ge 0 ? $p + 27 : 0
    }
}
$result
