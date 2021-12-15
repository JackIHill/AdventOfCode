
with open(r'2021/day_2/divedata.txt', 'r') as f:
    commands = [command.strip() for command in f.readlines()]

def part1(instructions):
    horiz_pos = 0
    depth = 0

    for line in instructions:
        movement, value = line.split()

        if movement == 'forward':
            horiz_pos += int(value)
        elif movement == 'down':
            depth += int(value)
        else:
            depth -= int(value)
    return horiz_pos * depth


def part2(instructions):
    horiz_pos = 0
    depth = 0
    aim = 0

    for line in instructions:
        movement, value = line.split()

        if movement == 'forward':
            horiz_pos += int(value)
            depth += aim * int(value)
        elif movement == 'down':
            aim += int(value)
        else:
            aim -= int(value)
    return horiz_pos * depth

print(f'Part 1 Result {part1(commands)}: ')
print(f'Part 2 Result: {part2(commands)}: ')