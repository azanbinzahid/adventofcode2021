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

# print(arr2d)

ans = []
for i in range(x):
    for j in range(y):
        # up = (i, j-1)
        # down = (i, j+1)
        # right = (i+1, j)
        # left = (i-1, j)
        
        lowest = True

        if i != 0:
            if arr2d[i][j] >= arr2d[i-1][j]:
                lowest = False
        
        if i+1 < x:
            if arr2d[i][j] >= arr2d[i+1][j]:
                lowest = False

        if j != 0:
            if arr2d[i][j] >= arr2d[i][j-1]:
                lowest = False
        
        if j+1 < y:
            if arr2d[i][j] >= arr2d[i][j+1]:
                lowest = False

        if lowest:
            ans.append((arr2d[i][j])+1)

print(sum(ans))