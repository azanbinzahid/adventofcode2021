import sys
MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize

global given
given = []
with open('in.txt', 'r') as f:
    given = list(map(str.strip, f.readlines()))
    given = map(int, given[0].split(','))

# print(given)

def calc_fuel(diff):
    ans = 0
    cost = 1
    for i in range(1, diff):
        cost+=1
        ans +=cost
    
    return ans

def calc_cost(ideal):
    global given
    cost = 0
    for i in given:
        cost += 1 + calc_fuel(abs(ideal-i))
        # print(i, ideal, cost)
    
    return cost

ans = -1
min_val = MAX_INT
for i in range(max(given)):
    # if i == 5:
    calc = calc_cost(i)
    # print(i, calc)
    if min_val > calc:
        min_val = calc
        ans = i

print(ans, min_val)