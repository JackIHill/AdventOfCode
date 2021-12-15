
with open(r'2021/day_1/SonarSweepInput.txt', 'r') as sonar_data:
    depths = [int(depth.strip()) for depth in sonar_data.readlines()]

    window_sums = [sum(depths[i:i+3]) for i in range(len(depths))]
    
counter = 0
for i, depth in enumerate(window_sums):
    if int(depth) > int(window_sums[i-1]):
        counter += 1

print(counter)