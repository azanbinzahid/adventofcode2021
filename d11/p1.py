given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)
arr2d = []
for g in given:
    g = map(int, list(g))
    arr2d.append(g)

# print(arr2d)

x = len(arr2d)
y = len(arr2d[0])
flash = 0



steps = 100
for s in range(steps):
    for i in range(x):
        for j in range(y):
            arr2d[i][j] += 1

    hash_set = set()
    while(True):
        flag = True
        for i in range(x):
            for j in range(y):
                if arr2d[i][j] > 9 and (i, j) not in hash_set:
                    flash+=1
                    hash_set.add((i, j))
                    flag = False
                    # arr2d[i][j] = 0

                    if i != 0:
                        arr2d[i-1][j]+=1
                        if j!=0:
                            arr2d[i-1][j-1]+=1
                    
                    if i+1 < x:
                        arr2d[i+1][j]+=1
                        if j+1 < y:
                            arr2d[i+1][j+1]+=1

                    if j != 0:
                        arr2d[i][j-1]+=1
                        if i+1 < x:
                            arr2d[i+1][j-1]+=1

                    if j+1 < y:
                        arr2d[i][j+1]+=1
                        if i != 0:
                            arr2d[i-1][j+1]+=1
        if flag:
            break

    for a, b in hash_set:
        arr2d[a][b] = 0

    
    # print('---------')
    # print('step', s+1)
    # print(arr2d)
    # print(flash)

print(flash)