from os import system

with open("../task/present2", "rb") as f:
    data = f.read()

with open("present2_patched", "wb") as f:
    new_data = data[:0x174D] + b"\x74" + data[0x174E:]
    f.write(new_data)

system("chmod +x present2_patched")
system("./present2_patched")