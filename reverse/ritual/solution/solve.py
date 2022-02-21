flag_chars = "b"

for i in range(1, 8):
    flag_chars += chr(ord(flag_chars[i - 1]) + i - 1)

print("[*] The flag is: li2CTF{%s}" % (flag_chars))
