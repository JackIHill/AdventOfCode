
with open(r'2021/day_6/fishinput.txt', 'r') as f:
    fishies = [int(i) for i in f.read().split(',')]

def how_many_fish(days):
    day = 0
    while day < 80:
        for idx, fish in enumerate(fishies):
            if fish > 0:
                fishies[idx] -= 1
            else:            
                fishies[idx] = 6
                fishies.append(9)
        day += 1    

    return len(fishies)

print(how_many_fish(80))