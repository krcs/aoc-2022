$input = "./input.txt"

$c = 0
$result= @();
cat $input | % {
    if ($_.length -gt 0) {
        $c += $_
    } else {
        $result += $c
        $c = 0
    }
}
($result | sort)[-3..-1] | Measure-Object -Sum | Select-Object -ExpandProperty Sum
