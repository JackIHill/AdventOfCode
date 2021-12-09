
from typing import final


with open(r'2021/day_3/binaryinput.txt', 'r') as f:
    binaries = [line.strip() for line in f.readlines()]


gamma_rate_bin = ''
epsilon_bin = ''
for i in range(0, 12):
    val_count = 0
    for binary in binaries:
        if binary[i] == "1":
            val_count += 1
        else:
            val_count -= 1
    if val_count > 0:
        gamma_rate_bin += "1"
        epsilon_bin += "0"
    else:
        gamma_rate_bin += "0"
        epsilon_bin += "1"

final_gamma = int(gamma_rate_bin, 2)
final_eps = int(epsilon_bin, 2)

print(final_gamma * final_eps)