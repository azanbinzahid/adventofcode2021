given = []
with open('in.txt', 'r') as f:
    given = list(map(str.strip, f.readlines()))
    given = map(int, given[0].split(','))

hash_map = dict()
for i in range(9):
    hash_map[i] = 0

for g in given:
    hash_map[g]+=1

# print('Initial State: ', hash_map)

days = 80
zeros = hash_map[0]
for d in range(days):
    for i in range(1,9):
        if hash_map[i] != 0:
            temp = hash_map[i]
            hash_map[i] -= temp
            hash_map[i-1] += temp

    hash_map[8] += zeros
    hash_map[6] += zeros
    hash_map[0] -= zeros
    zeros = hash_map[0]
    # print('After Days', d+1, hash_map)


ans = 0
for k, v in hash_map.items():
    ans +=v

print(ans)


