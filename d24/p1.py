given = []
with open('in.txt', 'r') as f:
    given = list(map(str.strip, f.readlines()))


def inp(val):
    return val
def add(a, b):
    return a+b
def mul(a, b):
    return a*b
def div(a, b):
    return a//b
def mod(a, b):
    return a%b
def eql(a, b):
    return 1 if a==b else 0


# brute force, may take hours to complete. Not recommended. 
# However, instruction parsing is correct 
INPUT = '100000000000000'
while True:
    INPUT = int(INPUT) -1
    INPUT = str(INPUT)

    if '0' not in INPUT:
        i = 0
        ALU = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
        }
        
        for g in given:
            g = g.split()
            if len(g)==3:
                ins, a, b = g
                b = ALU[b] if b in ALU else int(b)
                ALU[a] = eval(ins)(ALU[a], b)
            else:
                ins, a = g
                ALU[a] = int(INPUT[i])
                i+=1
        
        if ALU['z'] == 0:
            print('ans --> ', INPUT, ALU)
            break

        print(INPUT, ALU)
    