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

    # print(int(l_value, 2))

def handle_length_type_0():
    global POS
    global BITS
    
    total_length = BITS[POS:POS+15]
    POS +=15

    start = POS
    total_length = int(total_length, 2)
    while POS - start < total_length:
        manage_packets()

def handle_length_type_1():
    global POS
    global BITS

    num_sub_packets = BITS[POS:POS+11]
    POS+=11

    num_sub_packets = int(num_sub_packets, 2)

    for _ in range(num_sub_packets):
        manage_packets()    


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
        handle_type_4()

    # handle operators
    else:
        length_type_id = BITS[POS]
        POS+=1

        if length_type_id == '0':
            handle_length_type_0()
        elif length_type_id == '1':
            handle_length_type_1()




given = []
with open('in.txt', 'r') as f:
    given = map(str.strip, f.readlines())[0]

for g in given:
    g = int(g, 16)
    g = bin(g)[2:].zfill(4)
    BITS += g


manage_packets()
print(VERSION_COUNT)