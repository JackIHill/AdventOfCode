
with open('2021/day_7/crabinput.txt') as f:
    positions = [int(f) for f in f.readline().split(',')]

from statistics import median


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

def crab_part2():
    pos = 0
    best_fuel = set()
    while pos < len(positions):
        for n in range(1, len(positions) + 1):
            total_fuel = 0
            for position in positions:
                fuel = abs(n-position)   
                total_fuel += fuel                

            best_fuel.add(total_fuel)
        
        pos += 1
        return (min(best_fuel))   
            
print(crab_part2())