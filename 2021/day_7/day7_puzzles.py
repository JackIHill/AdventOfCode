
with open('2021/day_7/crabinput.txt') as f:
    positions = [int(f) for f in f.readline().split(',')]

from statistics import median
import numpy as np
# original solution
def crab_part1():
    medians = median(positions)
    fuels = []
    for position in positions:
        if position <= medians:
            fuels.append(medians - position)
        else:
            fuels.append(position - medians)

    return sum(fuels)

# print(crab_part1())  

# for part 1, pass False to additive_fuel
def crabs(additive_fuel=True):
    pos = 0
    best_fuel = set()
    
    for n in range(min(positions), max(positions) + 1):
        total_fuel = 0
        for position in positions:
            if additive_fuel is True:
                fuel = abs(n-position) * (abs(n-position) + 1) // 2
            else:
                fuel = np.abs(n-position)
            total_fuel += fuel
        best_fuel.add(total_fuel)
    pos += 1

    return (min(best_fuel))   

print(crabs(additive_fuel=True))