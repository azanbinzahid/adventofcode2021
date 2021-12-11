import sys
MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize

global given
given = []
with open('in.txt', 'r') as f:
    given = list(map(str.strip, f.readlines()))
    given = map(int, given[0].split(','))

# print(given)

def calc_cost(ideal):
    global given
    cost = 0
    for i in given:
        cost+= abs(ideal-i)
    
    return cost

ans = -1
min_val = MAX_INT
for i in given:
    if min_val > calc_cost(i):
        min_val = calc_cost(i)
        ans = i

print(ans, min_val)