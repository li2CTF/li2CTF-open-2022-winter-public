import re
import asyncio
from string import ascii_letters, digits
from random import randint, choice

FLAG = "li2CTF{cl34rly_D0ne!_H0p3_u_d1dn'7_cl34n_17_by_urS3Lf!}"

HOST, PORT = '0.0.0.0', 21007
TASKS_COUNT = 25
ALPHABET = ascii_letters + digits
GARBAGE = ".,!$#-=&*/\|"


def gen_ranodm_string() -> str:
    tmp = "".join([choice(ALPHABET) if randint(1, 10) < 8 else choice(GARBAGE) for i in range(randint(30, 50))])
    return tmp


def clean_str(s: str) -> str:
    tmp = ""
    for sym in s:
        if sym in ALPHABET:
            tmp += sym
    return tmp


class CleanerServer(asyncio.Protocol):
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.working = True
        self.level = 0
        self.ans = ""

    def set_timer(self, time):
        if not self.working:
            return
        if hasattr(self, "timeout_handle"):
            self.timeout_handle.cancel()
        self.timeout_handle = self.loop.call_later(
            time, self._timeout,
        )

    def connection_made(self, transport):
        if not self.working:
            return
        self.peername = transport.get_extra_info('peername')
        print(f"[.] Connected: {self.peername}")
        self.transport = transport
        self.transport.write(b"Time to clean! I send you text - you send me back the text without any special symbols - only letters, numbers and spaces!\n")
        self.set_timer(60)
        self.make_task()

    def data_received(self, data):
        if not self.working:
            return
        data = data.decode().strip()
        self.check_answer(data)
    
    def make_task(self):
        if not self.working:
            return
        tmp = gen_ranodm_string()
        self.ans = clean_str(tmp)
        self.transport.write(f"{tmp}\n".encode())
        
    def check_answer(self, s):
        if not self.working:
            return
        if s.strip() == self.ans:
            self.level += 1
            if self.level == TASKS_COUNT:
                self.terminate(FLAG)
            else:
                self.make_task()
        else:
            self.terminate("Wrong answer")

    def connection_lost(self, exc=None):
        if not self.working:
            return
        self.working = False
        try:
            self.dialog_typer.cancel()
        except AttributeError:
            pass
        self.transport.close()
        print(f"[.] Aborted connection: {self.peername}")

    def _timeout(self):
        if self.transport.is_closing():
            return
        print(f"[!] Timed out connection: {self.peername}")
        self.transport.close()
    
    def terminate(self, s):
        if not self.working:
            return
        self.working = False
        self.transport.write(f"\n{s}\n".encode())
        print(f"Connection with {self.peername} aborted. Reason: {s if FLAG not in s else 'User got flag.'}")
        self.transport.close()


async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(CleanerServer, host, port)
    print(f"[*] Server is running!")
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))
