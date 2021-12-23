
from collections import Counter

with open('2021/week_2/day_14/polymerinput.txt') as f:
    polyinputs = [f.strip() for f in f.readlines()]

def base_poly_and_pairs():
    poly = polyinputs[0]

    keys = [pair[0:2] for pair in polyinputs[2:]]
    vals = [pair[6] for pair in polyinputs[2:]]

    pairs = {keys[i]: vals[i] for i in range(len(keys))}

    return poly, pairs

poly, pairs = base_poly_and_pairs()

def pair_insertion(steps, poly, pairs):
    for _ in range(steps):
        new_poly = []
        chunks = [poly[i:i+2] for i in range(len(poly)-1)]
        for c in chunks:
            if c in pairs.keys():
                new_poly += c[0] + pairs[c]

        new_poly.append(chunks[-1][1])
        poly = ''.join(new_poly)

    element_count = Counter(poly)
    return element_count.most_common()[0][1] - element_count.most_common()[-1][1]

print(pair_insertion(10, poly, pairs))





