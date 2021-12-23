const {readFileSync} = require('fs');
const input = readFileSync("input", "UTF-8")
const sections = input.trim().split('\n\n').map(s => s.split('\n'));
let part1, part2;

let points = new Set();
for (let line of sections[0]) {
    const [x, y] = line.split(',').map(s => +s);
    points.add(x + y * 10000);
}
for (let line of sections[1]) {
    let [axis, mark] = line.match(/\w(?==)|\d+/g);
    mark = +mark;
    let foldedPoints = new Set();
    points.forEach(p => {
        let px = p % 10000;
        let py = ~~(p / 10000);
        if (axis === 'x') {
            if (px > mark) {
                px = mark * 2 - px;
            }
        } else {
            if (py > mark) {
                py = mark * 2 - py;
            }
        }
        foldedPoints.add(px + py * 10000);
    })
    points = foldedPoints;
    if (!part1) {
        part1 = foldedPoints.size;
    }
}

const grid = [];
points.forEach(p => {
    let px = p % 10000;
    let py = ~~(p / 10000);
    if (!grid[py]) {
        grid[py] = (new Array(40)).fill(' ');
    }
    grid[py][px] = '\u2588';
})
part2 = '\n' + grid.map(gy => gy.join('')).join('\n');

console.log(`{part1: ${part1}, part2: ${part2}}`);