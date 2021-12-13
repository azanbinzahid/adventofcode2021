given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)

COST_MAPPING = {
    ')': 3, 
    ']': 57, 
    '}': 1197, 
    '>': 25137, 
}


cost = 0
for g in given:
    stack = []
    for s in g:
        # print(s, stack)
        if s in '{[<(':
            stack.append(s)
        else:
            chk = stack.pop()
            if chk+s in ['{}', '<>', '()', '[]']:
                pass
            else:
                # print(chk, s, 'error')
                cost+=COST_MAPPING[s]

                break

print(cost)
