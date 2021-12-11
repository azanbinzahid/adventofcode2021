


measurements = []
with open('p1.txt', 'r') as f:
    measurements = map(int, f.readlines())

count = 0
for i, m in enumerate(measurements):
    if i != 0:
        if measurements[i] > measurements[i-1]:
            count+=1
print(count)
