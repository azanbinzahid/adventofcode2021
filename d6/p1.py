from collections import Counter

given = []
with open('in.txt', 'r') as f:
    given = list(map(str.strip, f.readlines()))
    given = map(int, given[0].split(','))


# print(given)
for i in range(80):
    for i, g in enumerate(given):
        if g == 0:
            given[i] = 6
            given.append(9) # 1 will be subtracted
        else:
            given[i] -= 1
    # print(given)



print(len(given))