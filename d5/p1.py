from collections import Counter
import numpy as np

given = []
with open('sample.txt', 'r') as f:
    given = map(str.strip, f.readlines())

max_X = -1
max_Y = -1
for x in range(len(given)):
    temp = list(map(int, given[x].replace('->', ',').split(',')))
    max_X = max(temp[0], temp[2], max_X) 
    max_Y = max(temp[1], temp[3], max_Y) 
    given[x] = ((temp[0], temp[1]), ((temp[2], temp[3])))

hash_map = {}
for i in range(max_X+1):
    for j in range(max_Y+1): 
        hash_map[i,j] = 0 

print('=====')
for g in given:
    x1, y1 = g[0]
    x2, y2 = g[1]

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    if x1 == y1 and x2 == y2:
        for i in range(x1, x2+1):
            for j in range(y1, y2+1): 
                if i == j:        
                    hash_map[i,j] += 1 
                    print(i, j, hash_map[i, j])

    
print(sum(value > 1 for value in hash_map.values()))