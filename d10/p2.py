
given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

# print(given)

SCORE_MAPPING = {
    '(': 1, 
    '[': 2, 
    '{': 3, 
    '<': 4, 
}


cost = 0
all_scores = []
for g in given:
    stack = []
    score = 0
    for s in g:
        if s in '{[<(':
            stack.append(s)
        else:
            chk = stack.pop()
            if chk+s in ['{}', '<>', '()', '[]']:
                pass
            else:
                break
    else:
        for s in stack[::-1]:
            score = (score * 5) + SCORE_MAPPING[s]
        all_scores.append(score)


all_scores.sort()
print(all_scores[len(all_scores)/2])




