const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf8').trim().split(',').map(s => parseInt(s));

//part 1
const sorted = input.sort((a,b) => a - b)
const best = (sorted[499] + sorted[500]) / 2
const part1 = input.reduce((cost, pos) => cost + Math.abs(best - pos), 0)
console.log(part1)

//part 2
const summation = (n) => n * (n+1) / 2
const cost = (best) => input.reduce((cost, pos) => cost + summation(Math.abs(best - pos)), 0)
let last = Infinity, i = 0
while(true) {
    const val = cost(i)
    if(last < val) {
        break
    }
    last = val
    i++
}
const part2 = last;
console.log(part2)