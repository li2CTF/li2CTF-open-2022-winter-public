flag = "b"

for i in range(1, 8):
    flag += chr(ord(flag[i - 1]) + (i - 1))

print(flag)
