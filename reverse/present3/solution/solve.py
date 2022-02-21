from os import system
from pwnlib.util.packing import *

main_addr = 0x401150

with open("../task/present3", "rb") as f:
    data = f.read()

with open("present3_patched", "wb") as f:
    new_data = data[:0x18] + p64(main_addr) + data[0x20:]
    f.write(new_data)

system("chmod +x present3_patched")
system("./present3_patched")
