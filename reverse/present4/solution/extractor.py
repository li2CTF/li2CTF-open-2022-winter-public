FLAG_FUNCTION_OFFSET = 0x3061
FLAG_FUNCTION_LENGTH = 1184
XOR_DEADBEEF_OFFSET = 0x1123

with open("src/task.elf", "rb") as f:
    binary = f.read()
    binary = [int(n) for n in binary]


def xor_flag_func_data():
    global binary
    for i in range(FLAG_FUNCTION_LENGTH):
        if i % 4 == 0:
            q = 0xef
        elif i % 4 == 1:
            q = 0xbe
        elif i % 4 == 2:
            q = 0xad
        elif i % 4 == 3:
            q = 0xde
        binary[FLAG_FUNCTION_OFFSET + i] ^= q


xor_flag_func_data()

# A XOR 0 = A
for i in range(4):
    binary[XOR_DEADBEEF_OFFSET + i] = 0

res = b""
for b in binary:
    res += bytes([b])

with open("./src/task_unxored.elf", "wb") as f:
    f.write(res)
