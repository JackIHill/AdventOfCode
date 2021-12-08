
with open(r'2021/day_2/divedata.txt', 'r') as f:
    commands = [command.strip() for command in f.readlines()]

print(commands)