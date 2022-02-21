import json

PORT_SERVER = "21019"
PORT_CLIENT = "51337"
PORTS = (PORT_SERVER, PORT_CLIENT)


def xor_data(data: bytes, xorkey: bytes) -> bytes:
    result = b""
    xorkey_size = len(xorkey)

    for i in range(0, len(data)):
        result += bytes([data[i] ^ xorkey[i % xorkey_size]])

    return result


conversation = []
server_key = 0
server_keysize = 0
client_key = 0
client_keysize = 0


with open("traffic/result.json", "r") as f:
    packets = json.loads(f.read())

    for i, packet in enumerate(packets):
        if packet["_source"]["layers"]["tcp"]["tcp.srcport"] in PORTS and packet["_source"]["layers"]["tcp"]["tcp.dstport"] in PORTS:
            tmp = dict()
            tmp["src"] = packet["_source"]["layers"]["tcp"]["tcp.srcport"]
            tmp["dst"] = packet["_source"]["layers"]["tcp"]["tcp.dstport"]

            raw_data = bytes([int(c, 16) for c in packet["_source"]["layers"]["tcp"]["tcp.payload"].split(":")])
            raw_data = raw_data[:]
            tmp["data"] = raw_data

            if b"H3LL0!" in raw_data:
                if tmp["src"] == PORT_SERVER:
                    server_keysize = raw_data[23]
                    server_key = raw_data[29:29+server_keysize]
                elif tmp["src"] == PORT_CLIENT:
                    client_keysize = raw_data[23]
                    client_key = raw_data[29:29+client_keysize]

            conversation.append(tmp)

    for i, message in enumerate(conversation):
        payload = message["data"]
        if b"H3LL0!" not in payload:
            payload = xor_data(payload, server_key)
            payload = xor_data(payload, client_key)

        print(f"{message['src']} -> {message['dst']}: {payload}")
