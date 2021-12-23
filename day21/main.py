from itertools import product
import re
from collections import defaultdict
from functools import lru_cache

def deterministic():
    pos = [9, 6]
    score = [0, 0]
    die = 0
    turn = 0
    rolls = 0
    while score[0] < 1000 and score[1] < 1000:
        for r in range(3):
            die = die % 100 + 1
            pos[turn] += die
            rolls += 1
        pos[turn] = (pos[turn] - 1) % 10 + 1
        score[turn] += pos[turn]
        turn = (turn + 1) % 2
    return min(score) * rolls

print(deterministic())

def part_two(pos_one, pos_two):
    @lru_cache(None)
    def recur(pos, scores=(0, 0), turn=0):
        cur_pos, cur_scores = list(pos), list(scores)
        wins = [0, 0]
        for a, b, c in product((1, 2, 3), repeat=3):
            move = a + b + c
            cur_pos[turn] = (pos[turn] + move) % 10
            if cur_pos[turn] == 0:
                cur_pos[turn] = 10
            cur_scores[turn] = scores[turn] + cur_pos[turn]
            if cur_scores[turn] >= 21:
                wins[turn] += 1
            else:
                one, two = recur(tuple(cur_pos), tuple(cur_scores), 1-turn)
                wins[0] += one
                wins[1] += two
        return wins
    return max(recur((pos_one, pos_two)))

print(part_two(9, 6))