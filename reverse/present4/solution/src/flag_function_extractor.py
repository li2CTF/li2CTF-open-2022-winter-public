F_START = 0x1125
F_END = 0x14E9

with open("flag.elf", "rb") as f:
    data = f.read()

    data = data[F_START:F_END+1]

    n_data = [int(n) for n in data]

    print(n_data)

with open("flagFunc.o", "wb") as f:
    f.write(data)