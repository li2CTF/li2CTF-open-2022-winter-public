from os import system

with open("src/task_unxored.elf", "rb") as f:
    binary = f.read()
    binary = [int(n) for n in binary]

to_nop = []

# patch #1: exit(0xD1E)
to_nop.append((0x306F, 0x3080))

# patch #2: int 1E
to_nop.append((0x3080, 0x3082))

# patch #3: xor ebp, ebp; xor esp, esp
to_nop.append((0x3082, 0x3088))

# patch #4: mov rax, [0]
to_nop.append((0x3088, 0x308D))

# patch #5: jmp 1
to_nop.append((0x308D, 0x3094))

for area in to_nop:
    for i in range(area[0], area[1]):
        binary[i] = 0x90

res = b""
for b in binary:
    res += bytes([b])

with open("./src/task_patched.elf", "wb") as f:
    f.write(res)

system("chmod +x ./src/task_patched.elf")
system("./src/task_patched.elf")