lines = [line.strip("\n") for line in open("inputs/day01.txt")]
numeric_chars = [[char for char in line if char.isnumeric()] for line in lines]
ans = sum([int(li[0] + li[-1]) for li in numeric_chars])
print(ans)


digits = list(map(str, range(1, 10)))
to_digit_map = dict(zip("one two three four five six seven eight nine".split(), digits)) | dict(zip(digits, digits))

ans = 0
for line in lines:
    li = []
    for key, val in to_digit_map.items():
        if key in line:
            li.append((line.index(key), val))
            li.append((line.rindex(key), val))
    ans += int(min(li)[1] + max(li)[1])
print(ans)
