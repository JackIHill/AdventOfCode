
with open('2021/week_2/day_9/heightmaps.txt') as f:
    heights = [h.strip() for h in f]

for h in heights:
    lows = []
    for i, n in enumerate(h):
        if int(n) < (int(n) + 1):
            lows += n

    print(lows)