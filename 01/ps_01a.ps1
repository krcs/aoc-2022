$input = "./input.txt"

$c = 0
$max = 0;
cat $input | % {
    if ($_.length -gt 0) {
        $c+=$_
    } else {
        if ($c -gt $max) {
            $max=$c
        }
        $c = 0
    }
}
$max
