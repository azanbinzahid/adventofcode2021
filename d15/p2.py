import numpy as np
import collections
import heapq

given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)

arr2d = []
for g in given:
    g = map(int, list(g))
    arr2d.append(g)


arr2d = np.array(arr2d)
# print(arr2d)
# print(arr2d + 1)
# np.where(arr2d > 9, 1, arr2d)
# print(arr2d)

arr5x = []
for i in range(5):
    arr5x.append(arr2d)
    arr2d = arr2d+1
    arr2d = np.where(arr2d > 9, 1, arr2d)

full_map = [arr5x]
for i in range(4):
    row = []
    arr2d = arr5x[i+1]
    for j in range(5):
        row.append(arr2d)
        arr2d = arr2d+1
        arr2d = np.where(arr2d > 9, 1, arr2d)
    full_map.append(row)


full_full_map = []
for i in range(len(full_map)):
    full_full_map.append((np.hstack(full_map[i])))

arr2d = np.vstack(full_full_map)

import json 

with open('data.json', 'w') as f:
    json.dump(arr2d.tolist(), f)

# print(arr2d)
