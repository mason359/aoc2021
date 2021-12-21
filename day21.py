from aocutils import get_lines

from functools import cache

def problem1():
    pos = [int(line.split(': ')[1]) - 1 for line in get_lines(21)]
    scores = [0, 0]
    die = 0
    while True:
        for p in range(2):
            pos[p] += die * 3 + 6
            scores[p] += pos[p] % 10 + 1
            die += 3
            if scores[p] >= 1000:
                return die * min(scores)

def problem2():
    pos = tuple(int(line.split(': ')[1]) - 1 for line in get_lines(21))
    scores = (0, 0)
    return max(play_game(pos, scores, 3, 0))

@cache
def play_game(pos, scores, rolls, player):
    if rolls == 0:
        new_scores = tuple(scores[i] + pos[i] + 1 if int(player) == i else scores[i] for i in range(2))
        if new_scores[player] >= 21:
            return [not player, player]
        else:
            return play_game(pos, new_scores, 3, not player)
    else:
        total = [0, 0]
        for roll in range(1, 4):
            new_pos = tuple((pos[i] + roll) % 10 if int(player) == i else pos[i] for i in range(2))
            winning = play_game(new_pos, scores, rolls - 1, player)
            total[0] += winning[0]
            total[1] += winning[1]
        return total
