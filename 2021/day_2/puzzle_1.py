
with open(r'2021/day_2/divedata.txt', 'r') as f:
    commands = [command.strip() for command in f.readlines()]

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

def find_sub(instructions):
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

print(find_sub(commands))