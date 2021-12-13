
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


def oxy_co2_binary(binaries, bit_num, option):
    most_common = 0 
    least_common = 0

    if len(binaries) == 1:
        return binaries[0]

    else:
        for binary in binaries:
            if binary[bit_num] == "1":
                most_common += 1
                least_common -= 1
            else:
                most_common -= 1
                least_common += 1

        add_one_binary = [binary for binary in binaries if binary[bit_num] == "1"]
        add_zero_binary = [binary for binary in binaries if binary[bit_num] == "0"]
        
        if option == 'most':
            if most_common >= 0:
                binaries = add_one_binary
            else:
                binaries = add_zero_binary 

        elif option == 'least':
            if least_common <= 0:
                binaries = add_zero_binary
            else:
                binaries = add_one_binary

        else:
            return 'Enter a valid option ("most", or "least")'

    bit_num += 1
    return oxy_co2_binary(binaries, bit_num, option)   


def get_life_support_rating():
    return (int(oxy_co2_binary(binaries, 0, 'most'), 2) * int(oxy_co2_binary(binaries, 0, 'least'), 2))

print(get_life_support_rating())