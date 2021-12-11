from collections import Counter


bits = []
with open('in.txt', 'r') as f:
    bits = map(str.strip, f.readlines())

ans = {}
for i, b in enumerate(bits):
    if i == 0:
        for x in range(len(b)):
            ans[x] = []

    for j, bj in enumerate(b):
        ans[j].append(bj)

gamma_rate = int((''.join([Counter(v).most_common()[0][0] for k, v in ans.items()])),2)
epsilon_rate = int((''.join([Counter(v).most_common()[1][0] for k, v in ans.items()])),2)

print(gamma_rate)
print(epsilon_rate)

print(gamma_rate*epsilon_rate)