def xor_data(data: bytes, xorkey: bytes) -> bytes:
    result = b""
    xorkey_size = len(xorkey)

    for i in range(0, len(data)):
        result += bytes([data[i] ^ xorkey[i % xorkey_size]])

    return result

print(xor_data(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", b"\xde\xad\xbe\xef"))