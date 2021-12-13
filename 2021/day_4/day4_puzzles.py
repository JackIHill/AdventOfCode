
from collections import _OrderedDictValuesView
from os import sched_get_priority_max
from pprint import pprint

with open('2021/day_4/bingoinput.txt') as f:
    bingo = f.readlines()

order = [int(i) for i in bingo[0].split(',')]
boards = []

rows = [[int(i) for i in row.split()] for row in board.split('\n')]

# boards = dict.fromkeys(range(len(boards_nested)))
# boards = dict(zip(boards, boards_nested))

# print(order)

# for i, board in enumerate(boards_nested):
#     for line in board:
#         for n in line:
#             print(n)

# print(boards_nested)

# print(order)
print(board)