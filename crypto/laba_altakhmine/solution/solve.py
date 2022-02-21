from base64 import b64decode
from string import ascii_lowercase

data = "NmcgNjkgMzIgNDMgNTQgNDYgN2YgNDEgMzEgNGogNWogNmYgMzEgMzAgNWogNTQgMzQgNmggNWogNjUgNTQgMzAgNWogNGcgMzQgNjIgNDEgNWogNjIgNDEgNWogMzEgN2UgNWogNTAgMzQgMzQgNWogNjkgNGkgMjQgNTQgMjEgNzQgNTUgNzQgMzQgNTQgNDEgN2g="

data = b64decode(data.encode("ascii")).decode("ascii")

data = [c for c in data]

for shift in range(26):
    tmp = data.copy()
    for j, c in enumerate(tmp):
        if c in ascii_lowercase:
            tmp[j] = ascii_lowercase[((ord(tmp[j]) + shift) - ord('a')) % len(ascii_lowercase)]
    
    tmp = "".join(tmp)
    print(f"Checking {shift}:", end=' ')

    try:
        tmp = [chr(int(c, 16)) for c in tmp.split(" ")]
    except ValueError:
        print("Not a valid hex values")
        continue

    print("".join(tmp))
