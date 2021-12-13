given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

count  = 0
for g in given:
    g = g.split('|')[1].split()
    for s in g:
        if len(s) in [2, 3, 4, 7]:
            # print(g)
            count+=1

print(count)