const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.split('\r\n');

let elfs = [];
let sum = 0;

for (let line of lines) {
    if (line.length === 0) {
        elfs.push(sum);
        sum=0;
    } else
        sum += parseInt(line);
}

sorted = elfs.sort((a,b)=> a>=b? -1 : 1);

console.log(sorted[0]+sorted[1]+sorted[2]);
