from pwn import *
from time import sleep
from base64 import b32decode, b32encode

with open("flag.txt", "rb") as f:
    secret = b32encode(f.read()).decode()


io_server = listen(port=81337)
io_client = remote('0.0.0.0', 81337)


def client_message(message: str):
    io_client.sendline(message.encode())
    print(f"Client: {message}")
    sleep(0.5)


def server_message(message: str):
    io_server.sendline(message.encode())
    print(f"Server: {message}")
    sleep(0.5)


client_message("hi")
server_message("Hello.")
client_message("i ma to finish ur order. where iz ma money??")
server_message("You are out of your time. Send secret key first.")
client_message("understandable. gimme me 5 secondz")
sleep(4.5)
client_message(secret)
server_message("What is that?")
client_message("itz a base32 of secret. i like security.")
server_message("Very well. Goodbye.")
client_message("hey wha ab' money??")
client_message("son of a beach im gona very hack u!!1!!11!1!")
