from collections import Counter

given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)

template = given[0]
rules = {}

for g in given[2:]:
    k, v = g.split(' -> ')
    rules[k] = v

hash_map = {}
first = template[0]
second = template[-1]
for i, t in enumerate(template):
    if i != len(template) - 1:
        k = template[i:i+2]
        if k not in hash_map:
            hash_map[k] = 1
        else:
            hash_map[k] += 1

# print('steps', 0, hash_map)


steps = 40
for i in range(steps):
    keys = hash_map.keys()
    old = hash_map.copy()
    for k in keys:
        if k in rules:
            temp = old[k]

            k1 = k[0]+rules[k]
            if k1 not in hash_map:
                hash_map[k1] = temp
            else:
                hash_map[k1] += temp

            k2 = rules[k]+k[1]
            if k2 not in hash_map:
                hash_map[k2] = temp
            else:
                hash_map[k2] += temp

            hash_map[k] -= temp
            
    # print('steps', i+1, hash_map)

counter = {}

for k, v in hash_map.items():

    if k[0] not in counter:
        counter[k[0]] = v
    else:
        counter[k[0]] += v


counter[second]+=1
# print(counter)

counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)
# print(counter)

print(counter[0][1] - counter[-1][1])
