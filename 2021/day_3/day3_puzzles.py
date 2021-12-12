
from os import getgrouplist


with open(r'2021/day_3/binaryinput.txt', 'r') as f:
    binaries = [line.strip() for line in f.readlines()]


def get_power_consum(binaries):
    gamma_rate_bin = ''
    epsilon_bin = ''    

    for i in range(12):
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
    
    return int(gamma_rate_bin, 2) * int(epsilon_bin, 2)


def get_life_support_rating(binaries, bit_num):
    most_common = 0 

    if len(binaries) == 1:
        return binaries[0]

    else:
        for binary in binaries:
            if binary[bit_num] > "0":
                most_common += 1
            else:
                most_common -= 1

        if most_common >= 0:
            binaries = [binary for binary in binaries if binary[bit_num] == "1"]
        else:
            binaries = [binary for binary in binaries if binary[bit_num] == "0"]
        
    bit_num += 1

    return get_life_support_rating(binaries, bit_num)    



    # return int(oxy_rating, 2) * int(co2_rating)

# print(get_power_consum(binaries))

print(get_life_support_rating(binaries, 0))