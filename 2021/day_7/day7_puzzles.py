
with open('2021/day_7/crabinput.txt') as f:
    positions = [int(f) for f in f.readline().split(',')]

from statistics import median

median = median(positions)

listies = []
for position in positions:
    if position <= median:
        listies.append(int(median) - position)
    else:
        listies.append(position - int(median))

print(sum(listies))