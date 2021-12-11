


commands = []
with open('in.txt', 'r') as f:
    commands = map(str.strip, f.readlines())

X = 0
Y = 0
aim = 0
for c in commands:
    c = c.split()
    c[1] = int(c[1])
    if c[0] == 'forward':
        X+=c[1]
    elif c[0] == 'down':
        Y+=c[1]
    elif c[0] == 'up':
        Y-=c[1]

print(X*Y)