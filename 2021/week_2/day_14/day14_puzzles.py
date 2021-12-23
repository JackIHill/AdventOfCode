
from collections import Counter

with open('2021/week_2/day_14/polymerinput.txt') as f:
    polyinputs = [f.strip() for f in f.readlines()]

poly = polyinputs[0]

keys = [pair[0:2] for pair in polyinputs[2:]]
vals = [pair[6] for pair in polyinputs[2:]]

pairs = {keys[i]: vals[i] for i in range(len(keys))}


for _ in range(12):
    new_poly = []
    chunks = [poly[i] + poly[i+1] for i in range(len(poly)-1)]
    for i, c in enumerate(chunks):
        for key, value in pairs.items():
            if c == key:
                new_poly += c[0] + value

    new_poly.append(chunks[-1][1])
    poly = ''.join(new_poly)


element_count = Counter(poly)
print(element_count.most_common()[0][1] - element_count.most_common()[-1][1])







