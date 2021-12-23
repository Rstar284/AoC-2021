const input = await Deno.readTextFile("input")
let lines = input.split("\n").map((row) => row.split("-"));
const valid = new Map<string, string[]>();
lines.forEach((row) => {
    const [f1,s1] = row;
    const f = valid.get(f1) ?? [];
    const s = valid.get(s1) ?? [];
    valid.set(f1, [...f, s1]);
    valid.set(s1, [...s, f1]);
});
let count = 0;
const caves: (cave: string, path: string[]) => string[][] = (cave,path) => {
    if(cave === cave.toLowerCase() && path.includes(cave)) return [];
    if(cave === "end") return [[...path, "end"]];
    path = [...path, cave];
    return valid.get(cave)!.flatMap((cave1) => caves(cave1, path));
};
const dcaves: (cave: string, path: string, doubled: boolean) => void = (cave,path,doubled) => {
    if(cave === "end") {count++; return};
    if(cave === "start" || cave == cave.toLowerCase() && path.split(cave).length > 2 || cave === cave.toLowerCase() && path.split(cave).length > 1 && doubled) return;

  if (cave === cave.toLowerCase() && path.split(cave).length > 1) {
    path = path + cave + "-";
    valid.get(cave)?.forEach((cave1) => dcaves(cave1, path, true));
  } else {
    path = path + cave + "-";
    valid.get(cave)?.forEach((cave1) => dcaves(cave1, path, doubled));
  }
};

const paths = valid.get("start")!.flatMap((cave) => {
    return caves(cave, ["start"]);
});

const paths1 = valid.get("start")!.flatMap((cave) => {
    return dcaves(cave, "start-", false);
});

console.log(paths.length);
console.log(count);
