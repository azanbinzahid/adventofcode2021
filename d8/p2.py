given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())

count = 0
for g in given:
    ins = g.split('|')[0].split()
    out = g.split('|')[1].split()
    hash_map = {}
    for s in 'abcdefg':
        hash_map[s] = set()

    for s in ins:
        l = len(s)
        s = set(sorted(s))

        if l == 2:
            for alphabet in 'cf':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s
    
        elif l == 3:
            for alphabet in 'acf':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s

        elif l == 4:
            for alphabet in 'bcdf':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s

        elif l == 5:
            for alphabet in 'adg':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s

        elif l == 6:
            for alphabet in 'abfg':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s

        elif l == 7:
            for alphabet in 'abcdefg':
                hash_map[alphabet] = hash_map[alphabet].intersection(s) if len(hash_map[alphabet]) > 0 else s

    while(True):
        flag = True
        alone = set()
        for k, v in hash_map.items():
            if len(v) == 1:
                alone.update(v)                          

        for k, v in hash_map.items():
            if len(v) != 1:
                hash_map[k] = v.difference(alone)        
                flag = False

        if flag:
            break

    for k, v in hash_map.items():
        hash_map[k] = list(v)[0]

    ORIGINAL_MAPPINGS = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }

    CONVERTED_MAPPING = {}
    for k, v in ORIGINAL_MAPPINGS.items():
        k = ''.join(sorted([hash_map[x] for x in k]))
        CONVERTED_MAPPING[k] = v
    
    num = ''
    for s in out:
        s = ''.join(sorted(s))
        num += str(CONVERTED_MAPPING[s])
    
    count += int(num)

print(count)