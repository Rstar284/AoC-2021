use anyhow::{anyhow, Result};
use ndarray::prelude::*;

type ParseResult = Array2<u8>;

fn parse(data: &str) -> ParseResult {
    let grid = data.lines().map(|line| {
        line.as_bytes().to_vec()
    }).collect::<Vec<_>>();
    let nrows = grid.len();
    let ncols = grid[0].len();
    let mut matrix = Array::zeros((nrows, ncols));
    for (r, line) in grid.iter().enumerate() {
        for (c, val) in line.iter().enumerate() {
            matrix[[r, c]] = *val;
        }
    }
    matrix
}

fn step_right(mat: &Array2<u8>) -> Array2<u8> {
    let mut res = mat.clone();

    for r in 0..mat.nrows() {
        for c in 0..mat.ncols() {
            if mat[[r,c]] != b'>' {
                continue;
            }

            let c2 = (c + 1) % mat.ncols();
            if mat[[r,c2]] == b'.' {
                res[[r,c]] = b'.';
                res[[r,c2]] = b'>';
            }
        }
    }

    res
}

fn step_down(mat: &Array2<u8>) -> Array2<u8> {
    let mut res = mat.clone();

    for r in 0..mat.nrows() {
        let r2 = (r + 1) % mat.nrows();
        for c in 0..mat.ncols() {
            if mat[[r,c]] != b'v' {
                continue;
            }

            if mat[[r2,c]] == b'.' {
                res[[r,c]] = b'.';
                res[[r2,c]] = b'v';
            }
        }
    }

    res
}

fn part1(input: &ParseResult) -> i64 {
    let mut res = 0;
    let mut board = input.clone();

    loop {
        let board2 = step_right(&board);
        let board3 = step_down(&board2);
        res += 1;

        if board3 == board {
            break;
        }
        board = board3;
    }

    res
}

fn main() {
    let data = include_str!("./input");
    let parsed = parse(data);
    let answ1 = part1(&parsed);
    println!("Part 1: {}", answ1);
}