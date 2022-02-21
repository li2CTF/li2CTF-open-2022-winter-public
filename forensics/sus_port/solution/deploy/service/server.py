from pwn import *
from random import randint
from subprocess import run
import sys
import socket


def xor_data(data: bytes, xorkey: bytes) -> bytes:
    result = b""
    xorkey_size = len(xorkey)

    for i in range(0, len(data)):
        result += bytes([data[i] ^ xorkey[i % xorkey_size]])

    return result


class ThreadServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))


    def listen(self):
        self.sock.listen(100)
        print("Server is ready to accept connections.")
        while True:
            client, address = self.sock.accept()
            client.settimeout(2)
            threading.Thread(target=self.listenToClient, args=(client,address)).start()


    def listenToClient(self, client, address):
        try:
            self.work(client, address)
        except socket.timeout:
            print(f"Timeout with {address}")
            pass
        client.close()
        return

    def work(self, client, address):
        client_keysize = 0
        server_keysize = randint(2, 6)
        client_key = b""
        server_key = b""

        for _ in range(server_keysize):
            server_key += bytes([randint(1, 255)])

        # ----------------- get client key -----------------
        data = client.recv(1024)

        if data[0:7] != b"H3LL0!|":
            client.close()
            return

        if data[7:15] != b"MTD=XOR|":
            client.close()
            return

        if data[15:23] != b"KEYSIZE=":
            client.close()
            return

        client_keysize = data[23]

        if data[25:29] != b"KEY=":
            client.close()
            return

        client_key = data[29:29+client_keysize]
        # --------------------------------------------------

        # ----------------- send server key ----------------
        pl = b"H3LL0!|MTD=XOR|KEYZISE=" + bytes([server_keysize]) + b"|KEY=" + server_key

        client.send(pl)
        # --------------------------------------------------

        # ---------- get commands and execute 'em! ---------
        for _ in range(30):
            data = client.recv(512)

            data = xor_data(data, server_key)
            data = xor_data(data, client_key)

            if data[0:4] != b"CMD=":
                client.close()
                return

            cmd = data[4:7].decode()

            if data[8:16] != b"ARGSIZE=":
                client.close()
                return

            argsize = data[16]

            if data[18:22] != b"ARG=":
                client.close()
                return
            
            arg = data[22:22+argsize].decode()

            print(cmd, arg)

            if cmd == "LST":
                cmd_result = run(["ls", arg], stdout=PIPE, stderr=PIPE)
                output = cmd_result.stdout
            elif cmd == "CAT":
                cmd_result = run(["cat", arg], stdout=PIPE, stderr=PIPE)
                output = cmd_result.stdout
            elif cmd == "UPT":
                cmd_result = run(["uptime"], stdout=PIPE, stderr=PIPE)
                output = cmd_result.stdout    
            elif cmd == "BYE":
                client.close()
                return
            else:
                output = b"NO SUCH COMMAND"

            output = xor_data(output, client_key)
            output = xor_data(output, server_key)

            client.send(output)
        # --------------------------------------------------


if __name__ == "__main__":
    ThreadServer("0.0.0.0", 21019).listen()