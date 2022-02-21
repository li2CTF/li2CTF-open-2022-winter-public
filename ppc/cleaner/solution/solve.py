import socket
from string import ascii_letters, digits
from time import sleep

ALPHABET = ascii_letters + digits


def clean_str(s: str) -> str:
    tmp = ""
    for sym in s:
        if sym in ALPHABET:
            tmp += sym
    return tmp


sock = socket.socket()
sock.connect(("ctf.li2sites.ru", 21007))

print(sock.recv(1024).decode())
sleep(0.1)

while True:
    data = sock.recv(1024).decode()
    if "Wrong" in data:
        print(data)
        break
    elif data == "":
        print("Error occured. Please restart the script!")
    data = data.replace("\n", "")
    if "li2CTF" in data:
        print("================== Flag found! ==================")
        print(data)
        print("=================================================")
        sock.close()
        break
    cleaned = clean_str(data)
    print(f"{data} -> {cleaned}")
    sock.send(f"{cleaned}".encode("ascii"))
