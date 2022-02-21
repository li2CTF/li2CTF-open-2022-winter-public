from os import system

system("nasm -o work.o work.asm")

with open("work.o", "rb") as f:
    data = f.read()
    data = [int(n) for n in data]

    if len(data) % 4 != 0:
        data += [90] * (4 - len(data) % 4) 

    for i in range(len(data)):
        if i % 4 == 0:
            data[i] ^= 0xef
        elif i % 4 == 1:
            data[i] ^= 0xbe
        elif i % 4 == 2:
            data[i] ^= 0xad
        elif i % 4 == 3:
            data[i] ^= 0xde

    print(data)
    print(len(data))
    res = b""
    for b in data:
        res += bytes([b])

with open("workXored.o", "wb") as f:
    f.write(res)
