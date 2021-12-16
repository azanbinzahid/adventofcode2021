import sys

given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)

global arr2d
arr2d = []
for g in given:
    g = map(int, list(g))
    arr2d.append(g)

x = y = len(arr2d)
start = arr2d[0][0]

def move(x, y):
    # For 1st column
    for i in range(1, x):
        arr2d[i][0] += arr2d[i - 1][0]
 
    # For 1st row
    for j in range(1, y):
        arr2d[0][j] += arr2d[0][j - 1]
 
    # For rest of the 2d matrix
    for i in range(1, x):
        for j in range(1, y):
            arr2d[i][j] += min(arr2d[i - 1][j], arr2d[i][j - 1])
 
    # Returning the value in
    # last cell
    return arr2d[i][j]


print(move(x, y) - start)
