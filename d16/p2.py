import numpy as np
BITS = ""
POS = 0
VERSION_COUNT = 0

def handle_type_4():
    global POS
    global BITS

    l_value = ''
    lead = BITS[POS]
    POS+=1

    while True:
        l_value += BITS[POS:POS+4]
        POS+=4

        if lead == '0':
            break

        lead = BITS[POS]
        POS += 1

    return int(l_value, 2)

def handle_length_type_0():
    global POS
    global BITS
    
    total_length = BITS[POS:POS+15]
    POS +=15

    start = POS
    total_length = int(total_length, 2)

    sub_packets = []
    while POS - start < total_length:
        sub_packets.append(manage_packets())
    
    return sub_packets

def handle_length_type_1():
    global POS
    global BITS

    num_sub_packets = BITS[POS:POS+11]
    POS+=11

    num_sub_packets = int(num_sub_packets, 2)
    sub_packets = []
    for _ in range(num_sub_packets):
        sub_packets.append(manage_packets())

    return sub_packets


def manage_packets():
    global BITS
    global POS
    global VERSION_COUNT

    version = BITS[POS:POS+3]
    POS+=3
    
    type_id = BITS[POS:POS+3]
    POS+=3

    VERSION_COUNT += int(version, 2)

    type_id = int(type_id, 2)
    if type_id == 4:
        return handle_type_4()

    # handle operators
    else:
        length_type_id = BITS[POS]
        POS+=1
        value = []
        if length_type_id == '0':
            value = handle_length_type_0()
        elif length_type_id == '1':
            value = handle_length_type_1()

        if type_id == 0:
            value = sum(value)
        elif type_id == 1:
            value = np.prod(np.array(value))
        elif type_id == 2:
            value = min(value)
        elif type_id == 3:
            value = max(value)
        elif type_id == 5:
            value = 1 if value[0] > value[1] else 0
        elif type_id == 6:
            value = 1 if value[0] < value[1] else 0
        elif type_id == 7:
            value = 1 if value[0] == value[1] else 0

        return value


given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())[0]

# given = '9C0141080250320F1802104A08'

for g in given:
    g = int(g, 16)
    g = bin(g)[2:].zfill(4)
    BITS += g

ans = manage_packets()
print(ans)