
import pprint

with open('2021/day_4/bingoinput.txt') as f:
    bingo = f.readlines()

boards = [pprint.pprint(bingo[2:])]
order = [bingo[0].strip()]

for board in boards:
    print(board)