
with open(r'2021/week_1/day_6/fishinput.txt', 'r') as f:
    fishies = [int(i) for i in f.read().split(',')]

def how_many_fish(days):
    day = 0
    while day < days:
        for idx, fish in enumerate(fishies):
            if fish > 0:
                fishies[idx] -= 1
            else:              
                fishies[idx] = 6
                fishies.append(9)
        day += 1    

    return len(fishies)

# making comments due to struggling and needing to seek other people's solutions. 

# Going to instead keep track of the days until a fish will birth a new,
# and how many fish there are for each of those days. Also leaving my original
# solution (part 1) here. 

def how_many_fish_better(days):
    fish_counts = {}
    # set dict keys to number of days until birth
    for val in range(0, 9):
        fish_counts[val] = 0
    # set dict values to number of fish for each of those days
    for fish in fishies:
        fish_counts[fish] += 1

    for _ in range(days):
        # get starting number of fish at 0th day until birth, and initialise that to 0
        # each new day (as 'a 0 becomes a 6 and adds a new 8').
        num_zero = fish_counts[0]
        fish_counts[0] = 0

        # need to shift each number of fish down one (so 2s go to 1, 1s to 0 etc)
        for i in range(1, len(fish_counts)):
            fish_counts[i-1] += fish_counts[i]
            fish_counts[i] = 0

        # all 0's become 6's and 8's. 
        fish_counts[8] += num_zero
        fish_counts[6] += num_zero

    return sum(fish_counts.values())

# print(how_many_fish(80))
print(how_many_fish_better(256))