
with open(r'2021/day_1/SonarSweepInput.txt', 'r') as sonar_data:
    depths = [int(depth.strip()) for depth in sonar_data.readlines()]

counter = 0
for i, depth in enumerate(depths):
    if depth > depths[i-1]:
        counter += 1

print(counter) 