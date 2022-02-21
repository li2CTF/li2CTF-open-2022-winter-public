from pwn import *
from random import randint

CMDS = ["LST", "CAT", "UPT", "BYE"]


def xor_data(data: bytes, xorkey: bytes) -> bytes:
    result = b""
    xorkey_size = len(xorkey)

    for i in range(0, len(data)):
        result += bytes([data[i] ^ xorkey[i % xorkey_size]])

    return result


io = remote("ctf.li2sites.ru", 21019)

client_keysize = randint(2, 6)
server_keysize = 0
client_key = b""
server_key = b""

for i in range(client_keysize):
    client_key += bytes([randint(1, 255)])


# ----------------- send client key ----------------
pl = b"H3LL0!|MTD=XOR|KEYSIZE=" + bytes([client_keysize]) + b"|KEY=" + client_key
io.send(pl)
# --------------------------------------------------

# ----------------- get server key -----------------
data = io.recv(512)

server_keysize = data[23]

server_key = data[29:29+server_keysize]
# --------------------------------------------------

while True:
    print("COMMANDS:")
    print("1. LST <PATH>")
    print("2. CAT <PATH>")
    print("3. UPT")
    print("4. BYE")

    raw_str = input().strip()
    if " " in raw_str:
        cmd, arg = raw_str.split()
    else:
        cmd = raw_str
        arg = ""
    
    print(cmd, arg)

    if cmd in CMDS:
        pl = b"CMD=" + cmd.encode() + b"|ARGSIZE=" + p8(len(arg)) + b"|ARG=" + arg.encode()
        pl = xor_data(pl, client_key)
        pl = xor_data(pl, server_key)

    io.send(pl)

    result = io.recv(4096)
    result = xor_data(result, server_key)
    result = xor_data(result, client_key)
    print(result.decode())

    if cmd == "BYE":
        break
