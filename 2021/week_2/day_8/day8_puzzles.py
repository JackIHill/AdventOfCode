
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# the wire/segment connections are mixed up separately for each four-digit display
# b/g wires might be turned on (must be trying to output 1 because only number with 2)
# segments. Dont know which of b or g is meant to go to c or f though. 


with open('2021/day_8/segmentinput.txt') as f:
    segments = [[s.strip().split(' ') for s in segs.split(' | ')] for segs in f.readlines()]

def num_1478():
    counter = 0
    for seg in segments:
        for s in seg[1]:
            if len(s) in [2, 3, 4, 7]:
                counter += 1
    return counter

# print(num_1478())

def decode_segments():
    for i, seg in enumerate(segments):
        num_decoder = {key: '' for key in range(0, 10)}
        for s in seg[0]:
            print(num_decoder)
            print(i, s)

decode_segments()