from collections import Counter


bits = []
with open('in.txt', 'r') as f:
    bits = map(str.strip, f.readlines())

oxy_bits = co2_bits = bits 

curr = 0
while(len(oxy_bits)>1):
    ans = {}
    for i, b in enumerate(oxy_bits):
        if i == 0:
            for x in range(len(b)):
                ans[x] = []

        for j, bj in enumerate(b):
            ans[j].append(bj)
    
    counter = [Counter(v).most_common()[0][0] for k, v in ans.items()]
    oxy_bits = [x for x in oxy_bits if counter[curr]==x[curr]]
    curr+=1

curr = 0
while(len(co2_bits)>1):
    ans = {}
    for i, b in enumerate(co2_bits):
        if i == 0:
            for x in range(len(b)):
                ans[x] = []

        for j, bj in enumerate(b):
            ans[j].append(bj)

    counter = [Counter(v).most_common()[-1][0] for k, v in ans.items()]
    co2_bits = [x for x in co2_bits if counter[curr]==x[curr]]
    curr+=1

oxy = int(oxy_bits[0],2)
co2 = int(co2_bits[0],2)

print(oxy*co2)