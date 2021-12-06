
with open(r'2021/day_1/SonarSweepInput.txt', 'r') as sonar_data:
    depths = sonar_data.readlines()
    depths = [depth.strip() for depth in depths]

    counter = 0
    for i, depth in enumerate(depths):
        if int(depth) > int(depths[i-1]):
            counter += 1

print(counter)   
    


