measurements = []
with open('p1.txt', 'r') as f:
    measurements = map(int, f.readlines())

count = 0
for i, m in enumerate(measurements):
    if len(measurements[i+1:i+1+3]) < 3:
        break
    if sum(measurements[i:i+3]) < sum(measurements[i+1:i+1+3]):
        count+=1
print(count)
