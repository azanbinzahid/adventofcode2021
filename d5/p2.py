from collections import Counter
import numpy as np

given = []
with open('in.txt', 'r') as f:
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

for g in given:
    g = sorted(g, key=lambda element: (element[0], element[1]))
    x1, y1 = g[0]
    x2, y2 = g[1]

    if x1 == x2 or y1 == y2:
        for i in range(x1, x2+1):
            for j in range(y1, y2+1): 
                hash_map[i,j] += 1 

    elif y1 > y2:
        i = x1
        j = y1

        while(i <= x2 and j >= y2):
            hash_map[i,j] += 1 
            i+=1
            j-=1

    else:
        i = x1
        j = y1

        while(i <= x2 and j <= y2):
            hash_map[i,j] += 1 
            i+=1
            j+=1

print(sum(value > 1 for value in hash_map.values()))