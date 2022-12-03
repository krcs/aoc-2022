#
# Advent of Code 2022
# Day 3, part 2
# https://github.com/krcs/aoc-2022
#
$result = 0
$groups = @()
$idx = 0

cat "./input.txt" | % {
    $group += $_
    if ($idx%3 -eq 2) {
        $g1 = $group[0].ToCharArray() | select -Unique
        $g2 = $group[1].ToCharArray() | select -Unique
        $g3 = $group[2].ToCharArray() | select -Unique
        $items = $g1 | ? { $g2 -ccontains $_ } | ? { $g3 -ccontains $_ }
        $items | % {
            $result += ($p=('a'..'z').IndexOf([char]$_)) -ge 0 ? $p + 1  : 0
            $result += ($p=('A'..'Z').IndexOf([char]$_)) -ge 0 ? $p + 27 : 0
        }
        $group = @()
    }
    $idx++
}
$result
