lines = [line.strip("\n") for line in open("inputs/day02.txt")]


# Part One

bag_limit = {"red": 12, "green": 13, "blue": 14}

impossible_games = set()

for idx, game in enumerate(lines, 1):
    draws = game.split(":")[1].split(";")
    for draw in draws:
        colors = [txt.strip() for txt in draw.split(",")]
        for txt in colors:
            n, color = txt.split()

            if int(n) > bag_limit[color]:
                impossible_games.add(idx)


ans = sum([game for game in range(1, len(lines) + 1) if game not in impossible_games])
print(ans)


# Part Two

from collections import defaultdict


ans = 0
for idx, game in enumerate(lines, 1):
    colors_counter = defaultdict(int)
    draws = game.split(":")[1].split(";")
    for draw in draws:
        colors = [txt.strip() for txt in draw.split(",")]
        for txt in colors:
            n, color = txt.split()

            if int(n) > colors_counter[color]:
                colors_counter[color] = int(n)
    
    product = 1
    for count in colors_counter.values():
        product *= count

    ans += product

print(ans)
