from numpy import prod

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
basins = {}

def find_more(begin, i, j):
    if (i, j) not in basins[begin]:
        basins[begin].add((i, j))
    else:
        return

    if i != 0:
        if arr2d[i][j]< arr2d[i-1][j] and arr2d[i-1][j] < 9:
            find_more(begin, i-1, j)
    
    if i+1 < x:
        if arr2d[i][j]< arr2d[i+1][j] and arr2d[i+1][j] < 9:
            find_more(begin, i+1, j)

    if j != 0:
        if arr2d[i][j]< arr2d[i][j-1] and arr2d[i][j-1] < 9:
            find_more(begin, i, j-1)
    
    if j+1 < y:
        if arr2d[i][j]< arr2d[i][j+1] and  arr2d[i][j+1] < 9:
            find_more(begin, i, j+1)

    


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
            # start navigation from here in all directions. 
            # assign unique basin id to i, j 
            basins[(i, j)] = set()
            find_more((i, j), i, j)


# visualize basins
# for i in range(x):
#     arr =  []
#     for j in range(y):
#         if (i, j) in common:
#             arr.append('*')
#         else:
#             arr.append('.')
#     print(arr)

basins = sorted(basins.values(), key = lambda x: len(x), reverse=True)[:3]
all_len = [len(s) for s in basins]
print(prod(all_len))