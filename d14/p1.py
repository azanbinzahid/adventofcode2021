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

steps = 10
temp = []
for i in range(steps):

    polymer = []
    for i, t in enumerate(template):
        if i != len(template) - 1:
            k = template[i:i+2]
            if k in rules:
                polymer.append((i+1,rules[k]))


    curr = 0
    temp = list(template)
    for p, v in polymer:
        temp.insert(p+curr, v)    
        curr+=1

    template = ''.join(temp)
    # print(template)

counter = Counter(temp).most_common()
most = counter[0][1]
least = counter[-1][1]
print(counter)
print(most-least)