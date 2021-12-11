from collections import Counter
import numpy as np

given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

order = map(int, given[0].split(','))

global boards

boards = {}
count = 0

def check_win():
    global boards
    for k, v in boards.items():
        arr_2d = np.array(boards[k]['np'])
        row = np.all((arr_2d == 1), axis=0)
        col = np.all((arr_2d == 1), axis=1)
        row_count = np.count_nonzero(row)
        col_count = np.count_nonzero(col)

        if row_count or col_count:
            return k

    return -1


for i, g in enumerate(given):
    if i == 0:
        continue
    
    elif g == '':
        count += 1
        boards[count] = {
            'arr': [],
            'np': [],
            'sum': 0
        }     

    else:
        row = map(int, g.split())
        # row = [[x, False] for x in row]
        boards[count]['arr'].append(row)
        boards[count]['np'].append([0 for x in row])

for o in order:
    for k, v in boards.items():
        for i in range(5):
            for j in range(5):
                if boards[k]['arr'][i][j] == o:
                     boards[k]['np'][i][j] = 1
                
                # elif boards[k]['np'][i][j] == 0:
                #     boards[k]['sum'] += boards[k]['arr'][i][j]


    k = check_win()
    if k != -1:
        for i in range(5):
            for j in range(5):
                if boards[k]['arr'][i][j] == o:
                     boards[k]['np'][i][j] = 1
                
                if boards[k]['np'][i][j] == 0:
                    boards[k]['sum'] += boards[k]['arr'][i][j]

        print(k, boards[k]['sum'], o)
        print(boards[k]['sum']*o)
        break
    